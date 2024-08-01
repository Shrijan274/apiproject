from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserInfoManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff as True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser as True')
        return self.create_user(email, name, password, **extra_fields)

class UserInfo(AbstractBaseUser):
    name = models.CharField(max_length=35)
    age = models.IntegerField(null=True)
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class TokenVerification(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email