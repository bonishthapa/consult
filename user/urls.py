  
from django.urls import path,include
from user import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()

router.register('user', views.UserCreateApi, basename='user')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout/blacklist/', views.BlacklistTokenUpdateView.as_view(),name='blacklist'),
    path('api/',include(router.urls)),
]