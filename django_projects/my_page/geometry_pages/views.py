from django.shortcuts import render
from django.http import HttpResponse
from math import pi


def get_rectangle_area(request, width, height):
    square = width * height

    return HttpResponse(f"Площадь = {square}")


def get_square_area(request, width):
    square = width * width

    return HttpResponse(f'Площадь = {square}')


def get_circle_area(request, radius):
    square = (radius * radius) * pi

    return HttpResponse(f'Площадь = {square: .2f}')
