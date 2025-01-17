from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Todo
        fields = (
            'id',
            'uid',
            'title',
            'description',
            'duedate',
            'created',
            'completed'
        )
        