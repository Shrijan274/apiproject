# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ExampleModel
from .serializers import CustomExampleModelSerializer
from rest_framework.permissions import AllowAny

class ExampleModelViewSet(viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all()
    serializer_class = CustomExampleModelSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific instance with custom logic.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Example of adding custom logic
        custom_data = {
            'id': instance.id,
            'custom_field': serializer.data.get('custom_field'),  # Adding custom data
            'data': serializer.data
        }

        return Response(custom_data, status=status.HTTP_200_OK)
