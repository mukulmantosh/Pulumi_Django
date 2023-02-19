# Generated by Django 4.1.4 on 2023-02-19 05:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EC2Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_information', models.TextField(editable=False, null=True)),
                ('status', models.CharField(default='PENDING', editable=False, max_length=50)),
                ('resource_requested_on', models.DateTimeField(default=datetime.datetime(2023, 2, 19, 10, 37, 13, 852285), editable=False)),
                ('resource_allocation_on', models.DateTimeField(editable=False, null=True)),
                ('instance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.instancetype')),
                ('key_pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.keypair')),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.operatingsystem')),
                ('security_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.securitygroup')),
                ('subnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.subnet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vpc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.vpc')),
            ],
            options={
                'verbose_name': 'Elastic Compute (EC2)',
                'verbose_name_plural': 'EC2_Resources',
            },
        ),
    ]
