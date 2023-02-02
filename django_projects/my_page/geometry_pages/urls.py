from django.urls import path
from . import views

urlpatterns = [
    path('circle/<int:radius>/', views.get_circle_area, name='circle_str'),
    path('square/<int:width>/', views.get_square_area, name='square_str'),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle_str'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_redirect),
    path('get_square_area/<int:width>', views.get_square_area_redirect),
    path('get_circle_area/<int:radius>', views.get_circle_area_redirect)
]
