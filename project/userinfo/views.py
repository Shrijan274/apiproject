from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.mail import send_mail      #django send mail facility
from .serializers import UserInfoModelSerializer,UserNameSerializer,EditprofileSerializer,DetailprofileSerializer
from rest_framework import viewsets, status,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from userinfo.models import UserInfo,TokenVerification
from django.views.decorators.csrf import csrf_exempt
import random
from project import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import login_required
from userinfo.forms import UserInfoForm  
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



@csrf_exempt
def  registeruser(request):
    template_name='register.html'
    return render(request,template_name)

def loginpage(request):
    template_name='login.html'
    return render(request,template_name)

class UserInfoViewSet(viewsets.ModelViewSet):

    queryset=UserInfo.objects.all()
    serializer_class = UserInfoModelSerializer
    permission_classes=[AllowAny]

    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer=UserNameSerializer(instance)
        return Response(serializer.data)
    
    def list(self,request,*args,**kwargs):
        #instance = self.get_object()
        serializer=UserNameSerializer(self.get_queryset(),many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token=random.randint(1000, 9999)
            email = request.data.get('email')
            password = request.data.get('password')
            print('token: ',token)
            TokenVerification.objects.create(email=email, token=str(token))
            send_mail(
                'Verify your email',
                f'Your verification token is {token}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            request.session['otp_token'] = token
            request.session['email'] = email
            request.session['user_data'] = serializer.data
            request.session['password'] = (password)
            print('password: ',password)

            return Response({'message': 'Check the email to access the OTP'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def verify_otp(self, request, *args, **kwargs):
        otp = request.data.get('otp')
        email = request.session.get('email')
        token = request.session.get('otp_token')
        user_data = request.session.get('user_data')
        password = request.session.get('password')
        
        if otp == str(token) and email:
            serializer = self.get_serializer(data=user_data)
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(password)  # Set the password (hash it)
                user.save()
                # Clear session data
                request.session.pop('otp_token')
                request.session.pop('email')
                request.session.pop('user_data')
                request.session.pop('password')
                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    # sample send mail format
    # send_mail(
    #             'test',
    #             'This is a test email sent from Django.',
    #             settings.EMAIL_HOST_USER,
    #             shrijanlingam@gmail.com
    #             fail_silently=False,
    #         )

class UserLogin(APIView):
    permission_classes = [AllowAny]
    queryset=UserInfo.objects.all()
    serializer_class = UserInfoModelSerializer
    def post(self, request):
        email = request.data.get('email')
        password= request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            #return redirect ('/user/userindex/')
            return Response({'message': 'Login successful','redirect_url': '/user/userindex/'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@login_required
def userindex(request):
    template_name='userindex.html'
    return render(request,template_name)

def userlogout(request):
    logout(request)
    return render(request,'login.html')

# @login_required
class Userlist(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserNameSerializer
    queryset=UserInfo.objects.all()


def EditProfile(request):
    template_name='editprofile.html'
    return render(request,template_name)

class UserProfile(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailprofileSerializer
    queryset=UserInfo.objects.all()
    
