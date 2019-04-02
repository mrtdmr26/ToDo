from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creating basic model for ToDo APP
class Todo(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    duedate = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title