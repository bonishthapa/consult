from django.urls import path,include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()

router.register('student', views.StudentAPIView, basename='student')
# router.register('dashboard/stat', views.DashboardStatAPIView, basename='stat')


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/dashboard/stat/', views.DashboardStatAPIView.as_view({'get':'list'}), name='dashboard'),
]