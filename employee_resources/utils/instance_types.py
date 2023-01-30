import boto3

from modules.models import InstanceType


def retrieve_instance_types(self):
    self.stdout.write("Retrieving Instance Types...")
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instance_types = ec2.describe_instance_types()["InstanceTypes"]
    obj_lists = [InstanceType(name=instance_result["InstanceType"],
                              architecture=instance_result["ProcessorInfo"]["SupportedArchitectures"][0]) for
                 instance_result in instance_types]

    InstanceType.objects.bulk_create(obj_lists)
