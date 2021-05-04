from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
   
    path('',views.all_blogs, name='all_blogs'),

]