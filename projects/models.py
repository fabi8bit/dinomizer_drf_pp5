from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    status_choices = [
        ('Planned','Planned'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ]

    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True)
    expected_end_date = models.DateTimeField(null=True)
    image = models.ImageField(
        upload_to='images/', default='../default_project_img_n5va32', blank=True
    )
    status = models.CharField(max_length=32, choices=status_choices, default='Planned')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.project_name}'