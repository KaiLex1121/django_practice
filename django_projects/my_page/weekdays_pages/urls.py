from django.urls import path
from . import views

urlpatterns = [
    path('<weekday>/', views.get_todo_list)
    ]
