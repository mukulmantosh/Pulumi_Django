import json

import boto3

from modules.models import Subnet, VPC


def retrieve_subnet_info(self):
    self.stdout.write("Retrieving Subnets Information...")
    vpc_lists = VPC.objects.all()
    ec2 = boto3.client('ec2')
    subnets_lists = ec2.describe_subnets()['Subnets']
    for vpc in vpc_lists:
        for subnet_info in subnets_lists:
            try:
                subnet_name = subnet_info["Tags"][0]["Value"]
            except KeyError:
                subnet_name = ""
            if subnet_info["VpcId"] == vpc.vpc_id:
                availability_zone = subnet_info['AvailabilityZone']
                subnet_id = subnet_info["SubnetId"]
                try:
                    subnet_tags = json.dumps(subnet_info['Tags'])
                except KeyError:
                    subnet_tags = None

                Subnet.objects.create(availability_zone=availability_zone, name=subnet_name, subnet_id=subnet_id,
                                      extra_info=subnet_tags, vpc=vpc)
