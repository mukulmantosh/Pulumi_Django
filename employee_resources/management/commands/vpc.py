import json

import boto3

from modules.models import VPC


def retrieve_vpc_info(self):
    self.stdout.write("Retrieving VPC Information...")

    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs()
    vpc_lists = response['Vpcs']

    for vpc_info in vpc_lists:
        vpc_id = vpc_info['VpcId']

        try:
            vpc_name = vpc_info["Tags"][0]["Value"]
        except KeyError:
            vpc_name = ""
        try:
            vpc_tags = json.dumps(vpc_info["Tags"])
        except KeyError:
            vpc_tags = None

        VPC.objects.create(name=vpc_name, vpc_id=vpc_id, extra_info=vpc_tags)
        self.stdout.write("Inserted VPC Information...")

