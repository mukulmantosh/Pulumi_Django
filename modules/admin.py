from django.contrib import admin

from . import models

admin.site.register(models.InstanceType)
admin.site.register(models.OperatingSystem)
admin.site.register(models.VPC)
admin.site.register(models.Subnet)
admin.site.register(models.SecurityGroup)
admin.site.register(models.KeyPair)