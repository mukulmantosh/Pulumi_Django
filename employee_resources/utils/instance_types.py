import json

import boto3
from modules.models import InstanceType, OperatingSystem




def create_operating_system():
    OperatingSystem.objects.create(name="Amazon Linux 2")
    OperatingSystem.objects.create(name="Ubuntu 20.04 LTS")


def retrieve_instance_types(self):
    self.stdout.write("Retrieving Instance Types...")
    # amazon_os = OperatingSystem.objects.get(name="Amazon Linux 2")
    # for ec2_type in ec2_instance_types('ap-south-1'):
    #     InstanceType.objects.create(operating_system=amazon_os)
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instance_types = ec2.describe_instance_types()["InstanceTypes"]
    for instance_result in instance_types:
        print(instance_result["InstanceType"], instance_result["ProcessorInfo"]["SupportedArchitectures"][0])
        #print(instance_result["InstanceType"], instance_types["SupportedArchitectures"])
    #print(json.dumps(instance_types))
    # SupportedArchitectures, InstanceType






