from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    duedate = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"] #ordering by the created field

    #class ReadonlyMeta:
    #    readonly = ["created"]

    def __str__(self):
        return self.title