from .views import allphoto, index,photo_detail,category_photos
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('allphoto/', allphoto, name='allphoto'),
    path('photo/<int:pk>/',photo_detail, name='photo_detail'),
    path('category/<int:category_id>/',category_photos, name='category_photos'),

]
