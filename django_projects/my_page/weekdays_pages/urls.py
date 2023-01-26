from django.urls import path
from . import views

urlpatterns = [
    path('monday/', views.monday_todo),
    path('tuesday/', views.tuesday_todo)
    ]
