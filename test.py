import boto3
from datetime import datetime, timedelta
from pytz import timezone

AWS_REGION = "ap-south-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_NAME_TAG_VALUE = "1"
instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'tag:EXPIRE',
            'Values': [
                INSTANCE_NAME_TAG_VALUE
            ]
        }
    ]
)

current_date_time = datetime.now().astimezone(timezone('Asia/Kolkata'))
for instance in instances:
    instance_data = instance.id
    print(instance_data)
    instance_info = EC2_RESOURCE.Instance(instance_data)
    instance_launch_time = instance_info.launch_time

    for tags in instance_info.tags:
        if tags['Key'] == "ExpiryDuration":
            expire_duration_min = int(tags['Value'])
            expire_duration_scheduled = instance_launch_time + timedelta(minutes=expire_duration_min)
            expire_duration_scheduled = expire_duration_scheduled.astimezone(timezone('Asia/Kolkata'))
            result = expire_duration_scheduled - current_date_time
            minutes = result.total_seconds() / 60
            if minutes > 0:
                print('Total difference in minutes: ', minutes)
            else:
                print("Instance Expired")
                instance_info.terminate()




