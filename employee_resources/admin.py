from django.contrib import admin
from . import models


class EC2ResourcesAdmin(admin.ModelAdmin):
    model = models.EC2Resources
    list_display = ['user', 'instance_type', 'operating_system', 'vpc',
                    'resource_requested_on', 'resource_allocation_on', 'resource_information', 'status']


admin.site.register(models.EC2Resources, EC2ResourcesAdmin)
admin.site.site_header = 'AWS Resource Management'
