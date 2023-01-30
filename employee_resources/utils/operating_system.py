import boto3

from modules.models import OperatingSystem


def create_operating_system(self):
    ec2_client = boto3.client('ec2', region_name='ap-south-1')
    images = ec2_client.describe_images(Owners=['amazon'])

    obj_lists = [OperatingSystem(name=result["Name"],
                                 architecture=result["Architecture"],
                                 image_id=result["ImageId"],
                                 expiry=result["DeprecationTime"]) for result in images["Images"]]

    OperatingSystem.objects.bulk_create(obj_lists, batch_size=100)
