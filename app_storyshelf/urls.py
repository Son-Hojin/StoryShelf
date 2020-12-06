from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path("read/", views.read, name="read"),
    path("write/", views.write, name="write"),
]