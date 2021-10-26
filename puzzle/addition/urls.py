from django.urls import path
from . import views

urlpatterns = [
    path('',views.addition,name='addition'),
    
]