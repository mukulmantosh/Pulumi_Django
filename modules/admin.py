from django.contrib import admin

from . import models

admin.site.register(models.VPC)
admin.site.register(models.Subnet)
admin.site.register(models.SecurityGroup)
admin.site.register(models.KeyPair)


class OperatingSystemAdmin(admin.ModelAdmin):
    model = models.OperatingSystem
    list_display = ['name', 'architecture', 'image_id', 'expiry']


class InstanceTypeAdmin(admin.ModelAdmin):
    model = models.InstanceType
    list_display = ['name', 'architecture']


admin.site.register(models.OperatingSystem, OperatingSystemAdmin)
admin.site.register(models.InstanceType, InstanceTypeAdmin)
