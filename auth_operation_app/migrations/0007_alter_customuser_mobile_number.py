# Generated by Django 5.2.4 on 2025-07-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_operation_app', '0006_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
