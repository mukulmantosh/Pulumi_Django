import json

import boto3
from django.core.management.base import BaseCommand
from employee_resources.utils.instance_types import retrieve_instance_types
from employee_resources.utils.security_groups import retrieve_security_group_info
from employee_resources.utils.operating_system import create_operating_system

class Command(BaseCommand):
    help = 'Load AWS Resource Information into DB'

    def handle(self, *args, **kwargs):
        self.stdout.write("Dumping AWS resources into database...")
        create_operating_system(self)
        # vpc.retrieve_vpc_info(self)
        # subnets.retrieve_subnet_info(self)
        #retrieve_instance_types(self)
       #retrieve_security_group_info(self)


