import boto3
from django.core.management.base import BaseCommand


def ec2_instance_types(region_name):
    '''Yield all available EC2 instance types in region <region_name>'''
    ec2 = boto3.client('ec2', region_name=region_name)
    describe_args = {}
    while True:
        describe_result = ec2.describe_instance_types(**describe_args)
        yield from [i['InstanceType'] for i in describe_result['InstanceTypes']]
        if 'NextToken' not in describe_result:
            break
        describe_args['NextToken'] = describe_result['NextToken']


class Command(BaseCommand):
    help = 'Load AWS Resource Information into DB'

    def handle(self, *args, **kwargs):
        self.stdout.write("Dumping AWS resources into database...")
        # vpc.retrieve_vpc_info(self)
        # subnets.retrieve_subnet_info(self)

        # for ec2_type in ec2_instance_types('ap-south-1'):
        #     print(ec2_type)

        ec2_client = boto3.client('ec2', region_name='ap-southeast-1')  # Change as appropriate
        images = ec2_client.describe_images(Owners=['self'])
        print(images)

        # ec2 = boto3.client('ec2')
        # response = ec2.describe_vpcs()
        # vpc_lists = response['Vpcs']
        # print(vpc_lists)
        #
        # for vpc_info in vpc_lists:
        #     vpc_info = vpc_info['VpcId']
        #     subnets_lists = ec2.describe_subnets()['Subnets']
        #     for subnet_info in subnets_lists:
        #         #print(subnet_info['AvailabilityZone'])
        #         #print(subnet_info['SubnetId'])
        #         try:
        #             subnet_tags = subnet_info['Tags']
        #             #print(subnet_tags)
        #         except KeyError:
        #             ...
        #
        #     security_groups = ec2.describe_security_groups()
        #     print(security_groups)
        #     for sg_info in security_groups["SecurityGroups"]:
        #         print(sg_info["Description"], sg_info["GroupId"], sg_info["VpcId"])
