from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duedate = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title