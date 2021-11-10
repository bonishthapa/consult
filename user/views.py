from rest_framework.response import Response
import jwt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from user import serializers
from user.models import User
from user.serializers import CurrentUserSerializer, LogoutSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserCreateApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

# class ObtainTokenPairWithUsernameView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer    


class UserDetails(generics.GenericAPIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        user = request.user
        serializer = CurrentUserSerializer(user)
        return Response(serializer.data)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)        