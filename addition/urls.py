from django.urls import path
from . import views

urlpatterns = [
    path('',views.addition,name='addition'),
    path('inner_design',views.inner_design,name='inner-design'),
    
]