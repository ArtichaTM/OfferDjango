from django.urls import path

from . import views

urlpatterns = [
    path('', views.about),
    path('favicon.ico', views.favicon),
]
