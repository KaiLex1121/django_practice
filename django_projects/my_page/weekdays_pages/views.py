from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def get_todo_list(request, weekday):

    weekday = weekday.capitalize()

    if weekday in days:
        return HttpResponse(f"Today is {weekday} and i'll do nothing")

    return HttpResponseNotFound(f'Дня недели {weekday} не существует')


def get_todo_list_by_num(request, weekday_num):
    if 1 <= weekday_num <= 7:
        response = days[weekday_num-1]

        return HttpResponseRedirect(f'/weekdays/{response}')

    return HttpResponseNotFound(f'Дня недели {weekday_num} не существует')
