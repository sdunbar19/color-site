from .serializers import ImageSerializer, HSVSerializer
from .models import Image, HSV
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .process_image import *

class ImageView(APIView):
    def _get_img_absolute_path(self, image_name):
        cwd = os.getcwd()
        cwd_split = cwd.split(os.sep)
        cwd_split.append("media")
        cwd_split.append("post_images")
        cwd_split.append(image_name)
        absolute_path_to_file = os.sep.join(cwd_split)
        return absolute_path_to_file

    def _delete_all_images(self):
        data = Image.objects.all()
        for obj in data:
            absolute_path_to_file = self._get_img_absolute_path(obj.image.name.split("/")[-1])
            os.remove(absolute_path_to_file)
            obj.delete()

    def get(self, request, *args, **kwargs):
        posts = Image.objects.all()
        serializer = ImageSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = ImageSerializer(data=request.data)
        if posts_serializer.is_valid():
            self._delete_all_images()
            posts_serializer.save()
            data = process(self._get_img_absolute_path(posts_serializer.data['image'].split("/")[-1]))
            return Response(data, status=status.HTTP_201_CREATED)
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