from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def monday_todo(request):
    return HttpResponse("<h1> Monday TODO list </h1> <ul> <li> Do something cool </li> <li> Do something bad </li> </ul")

def tuesday_todo(request):
    return HttpResponse("<h1> Tuesday TODO list </h1> <p> I didn't plan anything today </p>")