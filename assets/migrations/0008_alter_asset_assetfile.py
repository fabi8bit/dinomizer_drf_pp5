# Generated by Django 3.2.21 on 2023-10-15 09:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_asset_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='assetfile',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Asset'),
        ),
    ]