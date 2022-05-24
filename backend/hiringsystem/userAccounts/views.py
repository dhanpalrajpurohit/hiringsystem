from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.


class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        user = Users.objects.get(email=email)
        token, _ = Token.objects.get_or_create(user=user)
        user = LoginSerializer(user, many=True)
        return JsonResponse(data={'token': token.key, 'user': user.data},
                        status=HTTP_200_OK)


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            token = Token.objects.get_or_create(email=user.email)
            user.save()
            return JsonResponse({'token': token.key, 'user': user},
                            status=HTTP_200_OK)
