from . import views
from django.urls import path

app_name = "TV"

urlpatterns = [
    path("", views.tv_main, name='tvmain'),
]
