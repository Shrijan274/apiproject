from django.urls import path
from app import views
from .views import signup,UserLogin,UserList
from app.views import sqlquery
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/signup/', signup.as_view(), name='signup'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/login/',UserLogin.as_view(), name='login'),
    path("", views.index, name="index"),
    path('userlist/',UserList.as_view(),name='userlist'),
    path('sqlquery/',views.sqlquery,name='sqlquery'),
]