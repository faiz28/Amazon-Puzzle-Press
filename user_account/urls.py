from django.urls import path
from . import views

urlpatterns = [
    # path('',views.login,name='login'),
    path('register',views.register,name='signup'),
    path('login',views.login,name='signin'),
    path('logout',views.logout,name='logout'),
  
]