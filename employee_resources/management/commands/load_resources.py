from django.core.management.base import BaseCommand

from employee_resources.management.commands import vpc, subnets


class Command(BaseCommand):
    help = 'Load AWS Resource Information into DB'

    def handle(self, *args, **kwargs):
        self.stdout.write("Dumping AWS resources into database...")
        vpc.retrieve_vpc_info(self)
        subnets.retrieve_subnet_info(self)


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
