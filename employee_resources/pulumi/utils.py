
import pulumi
import pulumi_aws as aws


def create_pulumi_program(subnet_id, security_group_id, operating_system, instance_type, key_pair):
    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[
            {"name": "name", "values": [operating_system]}
        ],
    )

    instance = aws.ec2.Instance(
        "temp-webapp",
        instance_type=instance_type,
        vpc_security_group_ids=[security_group_id],
        key_name=key_pair,
        subnet_id=subnet_id,
        ami=ami.id,
        tags={
            "Name": "TEMP_SERVER"
        }
    )

    pulumi.export("web-app-ip", instance.public_ip)
