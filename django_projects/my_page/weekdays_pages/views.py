from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_todo_list(request, weekday):

    weekday = weekday.capitalize()

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday')

    if weekday in days:
        return HttpResponse(f"Today is {weekday} and i'll do nothing")

    return HttpResponse(f'Дня недели {weekday} не существует')


def get_todo_list_by_num(request, weekday_num):
    if 1 <= weekday_num <= 7:
        return HttpResponse(f"Today is the {weekday_num} day of the week")
    return HttpResponse(f'Incorrect number - {weekday_num}')