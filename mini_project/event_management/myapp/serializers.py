from rest_framework import serializers
from .models import Register, AddEvent

# Serializer for Register Model
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'  # Include all fields in the model

# Serializer for AddEvent Model
class AddEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddEvent
        fields = '__all__'  # Include all fields in the model

    def get_upload_poster(self, obj):
        request = self.context.get('request')
        if obj.upload_poster:
            return request.build_absolute_uri(obj.upload_poster.url)
        return None