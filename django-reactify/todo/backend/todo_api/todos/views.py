# todos/views.py
from rest_framework import generics

from .models import ToDo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer