from rest_framework import serializers
from .models import CustomUser

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

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    