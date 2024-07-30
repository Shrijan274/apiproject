from rest_framework import serializers
from .models import CustomUser
from datetime import datetime


class CustomUserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        email=data.get('email')
        username=data.get('username')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        
        valid_email=('gmail.com','yahoo.com','microsoft.com')
        invalid_names=['baby','sweety','cutie','bullshit']
        
        if not any(email.endswith(domain) for domain in valid_email):
            raise serializers.ValidationError('Invalid email domain')
        if any(invalid_name in username for invalid_name in invalid_names):
            raise serializers.ValidationError('Invalid name in username')
        if any(invalid_name in first_name for invalid_name in invalid_names):
            raise serializers.ValidationError('Invalid name in first name')
        if any(invalid_name in last_name for invalid_name in invalid_names):
            raise serializers.ValidationError('Invalid name in last name')
        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    description = serializers.SerializerMethodField()      # if no method name here, defaulty it takes get_fieldname

    def get_description(self,obj):
        now = datetime.now()
        created_time = now.strftime('%Y-%m-%d %H:%M:%S') 
        return f"{obj.email} is registered at {created_time}"

    class Meta:
        model = CustomUser
        #fields = '__all__'
        fields = ['email', 'username', 'first_name', 'last_name', 'password','description']
        extra_kwargs = {'password': {'write_only': True}}

