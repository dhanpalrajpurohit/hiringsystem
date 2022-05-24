from rest_framework import serializers
# from django.contrib.auth.models import User
#
from .models import Users


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = Users
        fields = ('email', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password', 'is_Candidate', 'is_Company')

    def create(self, validated_data):
        user = Users.objects.get(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user