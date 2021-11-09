from django.urls import path,include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()

router.register('student', views.StudentAPIView, basename='student')


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/filter/gender/<str:gender>/', views.GenderList.as_view(),name='gender'),
    path('api/filter/status/<str:status>/', views.StatusList.as_view(),name='status'),
    path('api/filter/level/<str:level>/', views.LevelList.as_view(),name='level'),

]