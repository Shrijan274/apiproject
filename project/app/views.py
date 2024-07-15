from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication
from app.service import jwt_generate_token
from rest_framework_jwt.settings import api_settings

#signup token
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImIyQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiYjIiLCJleHAiOjE3MjEwNzIxODIsIm9yaWdfaWF0IjoxNzIxMDcxODgyfQ.dVDzbZtzXOpQB5t71Gb-PIeA-ewUdTGIPROfecpgGSo

class signup(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #print(19,user.__dict__)
            #print(20,serializer)
            token=jwt_generate_token(user)
            print('token : ',token)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    authentication_classes=[BasicAuthentication]
    permission_classes=[AllowAny]

#class TokenObtainPairView(APIView):
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    permission_classes=[IsAuthenticated]
    


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

def index(request):
    template_name="index.html"
    return render(request, template_name)