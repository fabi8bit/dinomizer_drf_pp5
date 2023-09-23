from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset


class Check(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_id = models.ForeignKey(
        Asset, related_name='check_asset', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'asset_id']

    def __str__(self):
        return f'{self.owner} {self.asset}'