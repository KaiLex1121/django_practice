from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_leo_sign(request):
    return HttpResponse('Лев')


def show_aries_sign(request):
    return HttpResponse('Овен')


def show_taurus_sign(request):
    return HttpResponse('Телец')