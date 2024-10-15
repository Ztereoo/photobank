from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Photo


def index(request):
    return HttpResponse('This is index page')


def allphoto(request):
    photo= Photo.objects.all()
    paginator = Paginator(photo, 6)  # Отображать по 6 фото на странице (можете изменить количество)

    page_number = request.GET.get('page')  # Получить номер страницы из запроса
    page_obj = paginator.get_page(page_number)
    return render(request, 'allphoto.html', {'photo': photo,'page_obj':page_obj})

def photo_detail(request,pk):
    photo=get_object_or_404(Photo,pk=pk)
    return (request,'photo_detail.html', {'photo':photo})


