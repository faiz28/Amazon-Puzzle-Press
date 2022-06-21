from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.wordsearch,name='wordsearch'),
    path('inner_design',views.wordsearch_design,name='wordsearch-design'),    
]