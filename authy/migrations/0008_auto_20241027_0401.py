# Generated by Django 3.1 on 2024-10-26 22:31

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0007_auto_20241027_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pic/default.jpg', null=True, upload_to=authy.models.user_directory_path),
        ),
    ]
