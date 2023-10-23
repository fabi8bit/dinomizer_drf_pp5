from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_id = models.ForeignKey(
        Asset, related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
