from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class InstanceType(models.Model):
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class VPC(models.Model):
    vpc_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    extra_info = models.JSONField(null=True, editable=False)

    def __str__(self):
        return f"({self.vpc_id}) - {self.name}"


class Subnet(models.Model):
    name = models.CharField(max_length=100)
    subnet_id = models.CharField(max_length=100)
    vpc = models.ForeignKey(VPC, on_delete=models.CASCADE)
    availability_zone = models.CharField(max_length=100)
    extra_info = models.JSONField(null=True)

    def __str__(self):
        return f"{self.name} - ({self.vpc.vpc_id})"


class SecurityGroup(models.Model):
    name = models.CharField(max_length=500)
    security_group_id = models.CharField(max_length=200)
    vpc = models.ForeignKey(VPC, on_delete=models.CASCADE)
    extra_info = models.TextField(null=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.name} - ({self.security_group_id})"


class KeyPair(models.Model):
    name = models.CharField(max_length=100)
    keypair_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.keypair_id}"
