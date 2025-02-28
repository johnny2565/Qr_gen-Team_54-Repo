# Generated by Django 4.0.6 on 2022-08-03 21:21

import apps.common.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to='images/', validators=[apps.common.custom_validators.validate_image_file_type]),
        ),
    ]
