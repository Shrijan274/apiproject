from django.urls import path, include
from app import views
from .views import signup,UserLogin,UserList,index
from app.views import sqlquery
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/signup/', signup.as_view(), name='signup'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/login/',UserLogin.as_view(), name='login'),
    path('userlist/',UserList.as_view(),name='userlist'),
    path('sqlquery/',views.sqlquery,name='sqlquery'),
    path('joins/',views.joins,name='sqlquery'),
    path("", index.as_view(), name="index"),


]