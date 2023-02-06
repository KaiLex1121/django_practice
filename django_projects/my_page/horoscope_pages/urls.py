from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index),
    path('type/', views.get_type_page),
    path('type/<element>/', views.get_signs_by_elements, name='signs_by_element'),
    path('<int:day>/<int:month>/', views.get_sign_by_date),
    path('<int:zodiac_number>/', views.get_zodiac_sign_by_num),
    path('<str:zodiac_sign>/', views.get_zodiac_sign, name='horoscope_zodiac_sign'),
]
