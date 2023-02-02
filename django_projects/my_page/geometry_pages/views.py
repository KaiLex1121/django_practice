from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


def get_rectangle_area(request, width, height):
    square = width * height

    return HttpResponse(f"Площадь = {square}")


def get_rectangle_area_redirect(request, width, height):
    redirect_url = reverse('rectangle_str', args=(width, height))

    return HttpResponseRedirect(redirect_url)


def get_square_area(request, width):
    square = width * width

    return HttpResponse(f'Площадь = {square}')


def get_square_area_redirect(request, width):
    redirect_url = reverse('square_str', args=(width,))

    return HttpResponseRedirect(redirect_url)


def get_circle_area(request, radius):
    square = (radius * radius) * pi

    return HttpResponse(f'Площадь = {square: .2f}')


def get_circle_area_redirect(request, radius):
    redirect_url = reverse('circle_str', args=(radius,))

    return HttpResponseRedirect(redirect_url)
