from django.contrib.auth import authenticate, login, logout
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import BasicAuthentication
from app.service import jwt_generate_token,jwt_token
from rest_framework_jwt.settings import api_settings
from app.models import CustomUser,Author,Book,Genre



class signup(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #print(19,user.__dict__)
            #print(20,serializer)
            #token=jwt_generate_token(user)
            #print('token : ',token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    authentication_classes=[BasicAuthentication]
    permission_classes=[AllowAny]

#@api_view(['POST'])
class UserLogin(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            global logintoken
            logintoken = jwt_token(user)
            login(request, user)
            print('token : ',logintoken)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

def index(request):
    template_name="index.html"
    return render(request, template_name)

class UserList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
