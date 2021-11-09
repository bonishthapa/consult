from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email','first_name','username','password','is_active','is_staff']