from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
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
