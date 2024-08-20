from django.contrib import admin
from django.urls import path,include 
from . import views
 

app_name = 'HOME'

urlpatterns = [
     path("", views.home, name='HomePage')    
 
]
