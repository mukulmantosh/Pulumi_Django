import boto3

from modules.models import KeyPair


def retrieve_key_pairs(self):
    self.stdout.write("Retrieving Key Pairs...")
    client = boto3.client('ec2', 'ap-south-1')

    key_pairs = client.describe_key_pairs()
    obj_list = [KeyPair(name=keypair_info["KeyName"], keypair_id=keypair_info["KeyPairId"]) for keypair_info in
                key_pairs["KeyPairs"]]
    KeyPair.objects.bulk_create(obj_list)
