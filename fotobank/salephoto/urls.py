from .views import allphoto, index,photo_detail
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('allphoto/', allphoto, name='allphoto'),
    path('photo/<int:pk>/',photo_detail, name='photo_detail')
]
