from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Taskserializers
from .models import Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class=Taskserializers

class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = Taskserializers

class completedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = Taskserializers