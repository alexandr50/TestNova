from django.shortcuts import render
from rest_framework import generics

from .models import File
from .serializers import FileCreateSerializer


class FileCreateView(generics.CreateAPIView):
    serializer_class = FileCreateSerializer
    queryset = File.objects.all()
