import pulumi
import pulumi_aws as aws
from django.shortcuts import HttpResponse
from django.views import View
from pulumi import automation as auto


def create_pulumi_program(content: str):
    # sg = aws.ec2.SecurityGroup('web-sg',
    #                            description='Enable HTTP access',
    #                            ingress=[aws.ec2.SecurityGroupIngressArgs(
    #                                protocol='tcp',
    #                                from_port=80,
    #                                to_port=80,
    #                                cidr_blocks=['0.0.0.0/0'],
    #                            )])

    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[{"name": "image-id", "values": ['ami-0491e5015eb6e7a9b']}],


    )
    print("AMI is ", ami.image_id)
    print(ami.architecture)
    print(ami.id)

    # user_data = """
    # #!/bin/bash
    # uname -n > index.html
    # nohup python -m SimpleHTTPServer 80 &
    # """
    #
    # instance = aws.ec2.Instance(
    #     "pulumi-webapp",
    #     instance_type="t2.micro",
    #     vpc_security_group_ids=[sg.id],
    #     ami=ami.id,
    #     user_data=user_data,
    #     tags={
    #         "Name": "test-server-1"
    #     }
    # )
    #
    # pulumi.export("web-app-ip", instance.public_ip)


class DataView(View):
    def get(self, request):
        def pulumi_program():
            return create_pulumi_program("Hello World")

        stack = auto.select_stack(stack_name="dev",
                                  project_name="aws-python",
                                  program=pulumi_program)
        stack.set_config("aws:region", auto.ConfigValue("ap-south-1"))
        # deploy the stack, tailing the logs to stdout
        up_res = stack.up(on_output=print)

        print(up_res)

        return HttpResponse("It Works !")
