# Generated by Django 3.2.21 on 2023-10-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_alter_asset_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(default='../default_asset_img_dwjzkq', upload_to='images/'),
        ),
    ]
