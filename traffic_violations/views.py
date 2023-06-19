from django.shortcuts import render
from .models import Citizens


def menu(request):
    return render(request, 'menu.html')


def citizens(request):
    citizens_objects = Citizens.objects.all()[0:1000]
    return render(request, 'citizens.html', {'citizens': citizens_objects})
