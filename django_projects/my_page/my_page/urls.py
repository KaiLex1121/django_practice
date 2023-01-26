"""horoscope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from horoscope_pages import views as horoscope_views
from weekdays_pages import views as weekdays_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/leo', horoscope_views.show_leo_sign),
    path('horoscope/aries', horoscope_views.show_aries_sign),
    path('horoscope/taurus', horoscope_views.show_taurus_sign),
    path('weekdays/monday', weekdays_views.monday_todo),
    path('weekdays/tuesday', weekdays_views.tuesday_todo)
]
