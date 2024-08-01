from django.urls import path, include
from userinfo.views import UserInfoViewSet,registeruser,UserLogin,userindex,Userlist,EditProfile,UserProfile
from rest_framework import permissions
from . import views

urlpatterns = [
    #path('',UserInfoViewSet.as_view({'get': 'list','post':'create'}),name='create_userdata'),
    #path('<int:pk>/',UserInfoViewSet.as_view({'get':'retrieve','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name='userdata'),
    path('', views.registeruser,name='registeruser'),
    path('create/',UserInfoViewSet.as_view({'get': 'list','post':'create'}),name='create_userdata'),
    path('verify-otp/', UserInfoViewSet.as_view({'post': 'verify_otp'}), name='verify_otp'),
    path('loginwork/',UserLogin.as_view(),name='Login'),
    path('login/',views.loginpage,name='loginpage'),
    path('userindex/',views.userindex,name='userindex'),
    path('logout/',views.userlogout,name='logout'),
    path('userlist/',Userlist.as_view(),name='userlist'),
#    path('edituser/<int:pk>',views.EditProfile,name='editprofile'),
    path('edituser/',views.EditProfile,name='editprofile'),
    path('userprofile/<int:pk>/',UserProfile.as_view(),name='userprofile')

]
