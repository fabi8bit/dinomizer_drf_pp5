# Generated by Django 3.2.21 on 2023-10-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_alter_asset_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='assetfile',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
