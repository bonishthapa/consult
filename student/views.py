from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters


# Create your views here.

class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenderList(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        gender = self.kwargs['gender']
        return Student.objects.filter(gender=gender)


class LevelList(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        level = self.kwargs['level']
        return Student.objects.filter(level=level)    


class StatusList(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        status = self.kwargs['status']
        return Student.objects.filter(status=status)