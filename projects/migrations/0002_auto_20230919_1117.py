# Generated by Django 3.2.21 on 2023-09-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='expected_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]