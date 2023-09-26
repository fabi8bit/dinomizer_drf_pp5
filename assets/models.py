from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Asset(models.Model):

    category_choices = [
        ('graphic','Graphic'),
        ('video','Video'),
        ('audio','Audio'),
        ('copywriting','Copywriting'),
        ('other','Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=32, choices=category_choices, default='G')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_asset_img_dwjzkq', blank=True
    )
    project_id = models.ForeignKey(
        Project, related_name='asset_project', null=False, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['asset_name', 'project_id']

    def __str__(self):
        return f'{self.asset_name}'
    