from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


def get_rectangle_area(request, width, height):
    square = width * height

    return HttpResponse(f"Площадь = {square}")


def get_rectangle_area_redirect(request, width, height):

    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area(request, width):
    square = width * width

    return HttpResponse(f'Площадь = {square}')


def get_square_area_redirect(request, width):

    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_circle_area(request, radius):
    square = (radius * radius) * pi

    return HttpResponse(f'Площадь = {square: .2f}')


def get_circle_area_redirect(request, radius):

    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
