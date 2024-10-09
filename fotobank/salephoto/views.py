from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is index page')


def allphoto(request):
    return render(request, 'allphoto.html', {'message': 'hello'})
