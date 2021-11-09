from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from rest_framework import viewsets
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