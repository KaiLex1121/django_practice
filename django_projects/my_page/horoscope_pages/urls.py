from django.urls import path
from . import views

urlpatterns = [
    path('leo/', views.show_leo_sign),
    path('aries/', views.show_aries_sign),
    path('taurus/', views.show_taurus_sign)
    ]