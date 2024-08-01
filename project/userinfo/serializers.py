from rest_framework import serializers
from .models import UserInfo

class UserInfoModelSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=UserInfo
        fields='__all__'
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserInfo.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate_email(self, value):
        if UserInfo.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=['pk','name','email']

class EditprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=['name','age','gender','address']

class DetailprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=['id','name','age','gender','address']