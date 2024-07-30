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
from django.db import connection
from django.http import JsonResponse
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle


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


class index(APIView):
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    def get(self,request):
        template_name="index.html"
        return render(request, template_name)
    
class UserList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

def sqlquery(request):
    value=request.GET.get('param',4)            
    with connection.cursor() as cursor:         # db connection
        cursor.execute("SELECT * FROM app_author WHERE id > %s ", [value])   #writing a raw query
        columns = [col[0] for col in cursor.description]        # getting the column names
        rows = cursor.fetchall()                    #getting the row data
    results = [dict(zip(columns,row)) for row in rows]      #converting to list of dictionaries
    #print(results)
    return JsonResponse(results,safe=False)     #false such that it allows list of dictionaries


from app.joins import teachercourses_teacher,teachercourses_courses,teacher_courses

def joins(request):
    with connection.cursor() as cursor:
        cursor.execute(teacher_courses)
        columns = [col[0] for col in cursor.description]        # getting the column names
        rows = cursor.fetchall()                    #getting the row data
        results = [dict(zip(columns,row)) for row in rows]
        return JsonResponse(results,safe=False)