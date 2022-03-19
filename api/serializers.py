# Django Rest Framework
from rest_framework import serializers

# Own
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""
    class Meta:
        model = Task
        fields = "__all__"
