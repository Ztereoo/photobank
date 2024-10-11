from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Photo


def index(request):
    return HttpResponse('This is index page')


def allphoto(request):
    photo= Photo.objects.all()
    return render(request, 'allphoto.html', {'photo': photo})

def photo_detail(request,pk):
    photo=get_object_or_404(Photo,pk=pk)
    return (request,'photo_detail.html', {'photo':photo})
