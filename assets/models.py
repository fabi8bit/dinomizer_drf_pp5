from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Asset(models.Model):

    category_choices = [
        ('graphic', 'graphic'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('copywriting', 'copywriting'),
        ('other', 'other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=32, choices=category_choices, default='other')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_asset_img_dwjzkq', blank=True
    )
    assetfile = CloudinaryField(
        "Asset",
        resource_type="auto",  # <= Options: image, video, raw, auto
    )
    project_id = models.ForeignKey(
        Project,
        related_name='asset_project',
        null=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.asset_name}'
