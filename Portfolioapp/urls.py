from importlib.resources import path
from unicodedata import name
from django.urls import path
from django import views
from.import views

urlpatterns = [
    path('',views.firstPage,name="firstpage"),
    path('MessegeData',views.MessegeData,name='MessegeData')
]
