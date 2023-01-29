import boto3

from modules.models import SecurityGroup, VPC


def retrieve_security_group_info(self):
    self.stdout.write("Retrieving Security Groups Information...")
    SecurityGroup.objects.filter().delete()
    vpc_lists = VPC.objects.all()
    ec2 = boto3.client('ec2')
    security_groups = ec2.describe_security_groups()
    for vpc in vpc_lists:
        for sg_info in security_groups["SecurityGroups"]:
            if vpc.vpc_id == sg_info["VpcId"]:
                SecurityGroup.objects.create(name=sg_info["Description"],
                                             security_group_id=sg_info["GroupId"],
                                             vpc=vpc)
