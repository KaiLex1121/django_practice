from django.urls import path
from . import views

urlpatterns = [
    path('<int:weekday_num>/', views.get_todo_list_by_num),
    path('<str:weekday>/', views.get_todo_list, name='weekday_str'),
    path('', views.get_main_page)
    ]
