from .serializers import ImageSerializer, HSVSerializer
from .models import Image, HSV
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ImageView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Image.objects.all()
        serializer = ImageSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = ImageSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class HSVView(APIView):
    def get(self, request, *args, **kwargs):
        posts = HSV.objects.all()
        serializer = HSVSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = HSVSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)