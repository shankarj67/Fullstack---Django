# todos/serializers.py
from rest_framework import serializers
from .models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = ToDo    