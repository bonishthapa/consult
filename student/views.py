from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    
    # def perform_create(self, serializer):
    #     print("create")
    #     obj = serializer.save()
    #     files=self.request.FILES.getlist('documents')
    #     print("file",files)
    #     for f in files:
    #         print("documents")
    #         mf = StudentFile.objects.create(documents=f)
    #         obj.documents.add(mf)
    
    # def get_queryset(self):
    #     return self.students.all()
