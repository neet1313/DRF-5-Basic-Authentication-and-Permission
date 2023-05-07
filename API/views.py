from django.shortcuts import render
from rest_framework import viewsets
from API import serializers, models
# Create your views here.

# ------- Model Serializer ------
class StudentViewset(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
