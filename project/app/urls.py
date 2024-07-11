from django.urls import path
from app import views
from .views import signup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/signup/', signup.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/logout/', views.logout_view, name='logout'),
    path("", views.index, name="index"),
]

"""
http://127.0.0.1:8000/api/signup/
{
   "email":"demo@gmail.com",
   "username":"demo",
   "first_name":"abc",
   "last_name":"def",
   "password":"demo"
}
"""
"""
http://127.0.0.1:8000/api/login/
{
     "email":"demo@gmail.com",
     "password":"demo"
}
"""