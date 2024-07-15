from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.ImageView.as_view(), name= 'image_list'),
    path('hsv/', views.HSVView.as_view(), name = "hsv_list"),
]