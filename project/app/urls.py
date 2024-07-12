from django.urls import path
from app import views
from .views import signup
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/signup/', signup.as_view(), name='signup'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/login/', obtain_jwt_token),
    path("", views.index, name="index"),
]