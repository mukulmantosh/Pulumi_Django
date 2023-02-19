from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pulumi import automation as auto

from employee_resources.pulumi.utils import create_pulumi_program
from modules.models import SecurityGroup, VPC, Subnet, KeyPair, OperatingSystem, InstanceType


class EC2Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instance_type = models.ForeignKey(InstanceType, on_delete=models.CASCADE)
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    vpc = models.ForeignKey(VPC, on_delete=models.CASCADE)
    subnet = models.ForeignKey(Subnet, on_delete=models.CASCADE)
    security_group = models.ForeignKey(SecurityGroup, on_delete=models.CASCADE)
    key_pair = models.ForeignKey(KeyPair, on_delete=models.CASCADE)
    resource_information = models.TextField(null=True, editable=False)
    status = models.CharField(max_length=50, default="PENDING", editable=False)
    resource_requested_on = models.DateTimeField(default=datetime.now(), editable=False)
    resource_allocation_on = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return f"EC2Resources - {self.id}"

    class Meta:
        verbose_name_plural = "EC2_Resources"
        verbose_name = "Elastic Compute (EC2)"

    def clean(self):
        if self.instance_type.architecture != self.operating_system.architecture:
            raise ValidationError("Architecture Mismatch !!! "
                                  "Instance Type and Operating System Architecture does not match.")


@receiver(post_save, sender=EC2Resources)
def create_ec2_resource(sender, instance, **kwargs):
    if instance.status == "CREATED":
        return

    subnet_id = instance.subnet.subnet_id
    security_group_id = instance.security_group.security_group_id
    operating_system = instance.operating_system.name
    instance_type = instance.instance_type.name
    key_pair = instance.key_pair.name

    def pulumi_program():
        return create_pulumi_program(subnet_id, security_group_id, operating_system, instance_type,
                                     key_pair)

    stack = auto.select_stack(stack_name=settings.PULUMI_STACK_NAME,  # <- Stack Name
                              project_name=settings.PULUMI_PROJECT_NAME,  # <- Name of the Pulumi Project
                              program=pulumi_program)
    stack.set_config("aws:region", auto.ConfigValue("ap-south-1"))

    launch_task = stack.up(on_output=print)
    instance.resource_information = launch_task.outputs["web-app-ip"]
    instance.resource_allocation_on = datetime.now()
    instance.status = "CREATED"
    instance.save()
    return


@receiver(post_delete, sender=EC2Resources)
def delete_ec2_resource(sender, instance, **kwargs):
    subnet_id = instance.subnet.subnet_id
    security_group_id = instance.security_group.security_group_id
    operating_system = instance.operating_system.name
    instance_type = instance.instance_type.name
    key_pair = instance.key_pair.name

    def pulumi_program():
        return create_pulumi_program(subnet_id, security_group_id, operating_system, instance_type,
                                     key_pair)

    stack = auto.select_stack(stack_name=settings.PULUMI_STACK_NAME,  # <- Stack Name
                              project_name=settings.PULUMI_PROJECT_NAME,  # <- Name of the Pulumi Project
                              program=pulumi_program)
    stack.set_config("aws:region", auto.ConfigValue("ap-south-1"))

    stack.destroy(on_output=print)
