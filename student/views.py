from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from student import serializers
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import response
from rest_framework import filters
from student.paginations import StudentPaginaition

# Create your views here.

class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = StudentPaginaition

    def get_queryset(self):
        queryset = Student.objects.all()
        gender = self.request.query_params.get('gender')
        level = self.request.query_params.get('level')
        status = self.request.query_params.get('status')

        if gender:
            queryset = queryset.filter(gender=gender)
        elif level:
            queryset = queryset.filter(level=level)
        elif status:
            queryset = queryset.filter(status=status)    

        return queryset

    def create(self, request, **kwargs):
        if self.request.user.is_active:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
             

    def update(self, request, **kwargs):
        if self.request.user.is_active:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = StudentSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)    

    #Add extra context in response
    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, args, kwargs)
    #     visa_granted = self.get_queryset().filter(status="Visa Granted").count()
    #     offer_pending = self.get_queryset().filter(status="Offer Pending").count()
    #     visa_pending = self.get_queryset().filter(status="Visa Pending").count()
    #     response.data['visa_granted'] = visa_granted
    #     response.data['offer_pending'] = offer_pending
    #     response.data['visa_pending'] = visa_pending
    #     return response

class DashboardStatAPIView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self,*args, **kwargs):
        queryset = Student.objects.all()
        total_student = queryset.count()
        visa_granted = queryset.filter(status="visa_granted").count()
        offer_pending = queryset.filter(status="offer_pending").count()
        visa_pending = queryset.filter(status="visa_pending").count()
        interview = queryset.filter(status="interview").count()
        cas_pending = queryset.filter(status="cas_pending").count()
        return Response({
            'total_student':total_student,
            'visa_granted':visa_granted,
            'offer_pending':offer_pending,
            'visa_pending':visa_pending,
            'interview':interview,
            'cas_pending':cas_pending,
            })

