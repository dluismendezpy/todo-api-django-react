# Django
from django.db import models


class Task(models.Model):
    """Model for all tasks"""
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    completed = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
