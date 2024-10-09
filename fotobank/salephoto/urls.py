from .views import allphoto, index
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('allphoto/', allphoto, name='allphoto'),
]
