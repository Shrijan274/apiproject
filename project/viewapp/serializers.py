# serializers.py
from rest_framework import serializers
from .models import ExampleModel
from datetime import datetime

class CustomExampleModelSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = ExampleModel
        fields = '__all__'

    def get_custom_field(self, obj):
        now = datetime.now()
        created_time = now.strftime('%Y-%m-%d %H:%M:%S') 
        return f"{obj.name} is retrieved at {created_time}"

