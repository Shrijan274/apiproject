from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from userinfo.models import UserInfo as UserInfo
from app.models import CustomUser as CustomUser
from django.contrib.auth.backends import ModelBackend

class UserInfoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(email=username)
            if user.check_password(password):  # Ensure your model has a password field
                return user
        except UserInfo.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserInfo.objects.get(pk=user_id)
        except UserInfo.DoesNotExist:
            return None

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None