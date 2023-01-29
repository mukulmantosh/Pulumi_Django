import boto3

from modules.models import OperatingSystem


def create_operating_system(self):
    #OperatingSystem.objects.create(name="Amazon Linux 2")
    #OperatingSystem.objects.create(name="Ubuntu 20.04 LTS")

    ec2_client = boto3.client('ec2', region_name='ap-south-1')
    images = ec2_client.describe_images(Owners=['amazon'])

    for result in images["Images"]:
        print(result["Architecture"], result["ImageId"], result["Name"], result["DeprecationTime"])
        break

    # print(images)
    # ImageId, Architecture, Name, Description

