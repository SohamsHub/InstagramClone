# Generated by Django 3.1 on 2024-10-26 21:51

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_auto_20241024_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to=authy.models.user_directory_path),
        ),
    ]
