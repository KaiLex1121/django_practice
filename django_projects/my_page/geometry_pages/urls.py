from django.urls import path
from . import views

urlpatterns = [
    path('circle/<int:radius>/', views.get_circle_area),
    path('square/<int:width>/', views.get_square_area),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area)
]
