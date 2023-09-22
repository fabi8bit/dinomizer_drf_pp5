from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Asset(models.Model):

    category_choices = [
        ('G','Graphic'),
        ('V','Video'),
        ('A','Audio'),
        ('CW','Copywriting'),
        ('O','Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=32, choices=category_choices, default='G')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_asset_img_dwjzkq', blank=True
    )
    projects = models.ManyToManyField(Project)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    