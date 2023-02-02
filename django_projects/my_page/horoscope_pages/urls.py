from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index),
    path('<int:zodiac_number>/', views.get_zodiac_sign_by_num),
    path('<str:zodiac_sign>/', views.get_zodiac_sign, name='horoscope_zodiac_sign')
]
