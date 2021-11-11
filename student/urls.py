from django.urls import path,include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()

router.register('student', views.StudentAPIView, basename='student')


urlpatterns = [
    path('api/',include(router.urls)),
]