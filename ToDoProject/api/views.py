from rest_framework import generics, permissions

from todos import models
from . import serializers





class ListTodo(generics.ListCreateAPIView):

    queryset = models.Todo.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    def get_queryset(self):
        return models.Todo.objects.all().filter(uid=self.request.user.pk)

    

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Todo.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    def get_queryset(self):
        return models.Todo.objects.all().filter(uid=self.request.user.pk)

    