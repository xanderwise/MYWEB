from django.contrib import admin
from django.urls import path

from webApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact, name='index'),
]
