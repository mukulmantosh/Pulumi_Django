import boto3

from modules.models import InstanceType

import boto3


def ec2_instance_types(region_name):
    """Yield all available EC2 instance types in region <region_name> """
    ec2 = boto3.client('ec2', region_name=region_name)
    describe_args = {}
    while True:
        describe_result = ec2.describe_instance_types(**describe_args)
        yield from [(i['InstanceType'], i["ProcessorInfo"]["SupportedArchitectures"][0]) for i in
                    describe_result['InstanceTypes']]
        if 'NextToken' not in describe_result:
            break
        describe_args['NextToken'] = describe_result['NextToken']


def retrieve_instance_types(self):
    self.stdout.write("Retrieving Instance Types...")
    obj_lists = [InstanceType(name=instance_result[0],
                              architecture=instance_result[1]) for instance_result in ec2_instance_types('ap-south-1')]
    InstanceType.objects.bulk_create(obj_lists)
