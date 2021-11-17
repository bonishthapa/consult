from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from student import serializers
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters
# from student.paginations import StudentPaginaition

# Create your views here.

class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # pagination_class = StudentPaginaition

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

# class DashboardStatAPIView(viewsets.ViewSet):
#     permission_classes = (IsAuthenticated,)

#     def list(self,*args, **kwargs):
#         queryset = Student.objects.all()
#         total_student = queryset.count()
#         visa_granted = queryset.filter(status="Visa Granted").count()
#         offer_pending = queryset.filter(status="Offer Pending").count()
#         visa_pending = queryset.filter(status="Visa Pending").count()
#         interview = queryset.filter(status="Interview").count()
#         cas_pending = queryset.filter(status="CAS Requested").count()
#         return Response({
#             'total_student':total_student,
#             'visa_granted':visa_granted,
#             'offer_pending':offer_pending,
#             'visa_pending':visa_pending,
#             'interview':interview,
#             'cas_pending':cas_pending,
#             })