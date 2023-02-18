from datetime import datetime

import pulumi
import pulumi_aws as aws
from django.shortcuts import HttpResponse
from django.views import View
from pulumi import automation as auto

from .models import EC2Resources


def create_pulumi_program(subnet_id, security_group_id, operating_system, instance_type, key_pair):
    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[
            {"name": "name", "values": [operating_system]}
        ],
    )

    print("NAME IS ", ami.image_id)
    instance = aws.ec2.Instance(
        "temp-em664-webapp",
        instance_type=instance_type,
        vpc_security_group_ids=[security_group_id],
        key_name=key_pair,
        subnet_id=subnet_id,
        ami=ami.id,
        tags={
            "Name": "EMP_664_TEMP_SERVER"
        }
    )

    pulumi.export("web-app-ip", instance.public_ip)


class CreatEC2ResourceView(View):
    def get(self, request):
        ec2_resource = EC2Resources.objects.first()
        vpc_id = ec2_resource.vpc.vpc_id
        subnet_id = ec2_resource.subnet.subnet_id
        security_group_id = ec2_resource.security_group.security_group_id
        operating_system = ec2_resource.operating_system.name
        instance_type = ec2_resource.instance_type.name
        key_pair = ec2_resource.key_pair.name
        print(vpc_id, subnet_id, security_group_id, operating_system, instance_type, key_pair)

        def pulumi_program():
            return create_pulumi_program(subnet_id, security_group_id, operating_system, instance_type,
                                         key_pair)

        stack = auto.select_stack(stack_name="dev",
                                  project_name="aws-python",
                                  program=pulumi_program)
        stack.set_config("aws:region", auto.ConfigValue("ap-south-1"))
        # deploy the stack, tailing the logs to stdout
        up_res = stack.destroy(on_output=print)

        # print(up_res.outputs["web-app-ip"])
        #
        # ec2_resource.resource_information = up_res.outputs["web-app-ip"]
        ec2_resource.resource_allocation_on = datetime.now()
        ec2_resource.status = "DELETED"
        ec2_resource.save()
        return HttpResponse("It Works !")
