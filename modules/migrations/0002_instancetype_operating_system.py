# Generated by Django 4.1.4 on 2022-12-25 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancetype',
            name='operating_system',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='modules.operatingsystem'),
            preserve_default=False,
        ),
    ]
