from rest_framework import serializers
from .models import Image, HSV

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class HSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSV
        fields = '__all__'