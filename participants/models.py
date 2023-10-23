from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Participant(models.Model):
    """
    Participant model, related to 'owner' and 'project_id'.
    'owner' is a User that participates on a Project.
    'Project_id' is a Project that is fed by 'owner'.
    'unique_together' makes sure a user can't 'double join'
    'the same project.
    """
    owner = models.ForeignKey(
        User, related_name='participant', on_delete=models.CASCADE
    )
    project_id = models.ForeignKey(
        Project, related_name='project', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'project_id']

    def __str__(self):
        return f'{self.owner} {self.project_id}'
