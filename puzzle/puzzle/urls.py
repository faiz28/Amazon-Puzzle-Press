from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import homepage.views

urlpatterns = [
    path('',homepage.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('upload/',include('upload.urls')),
    path('user_account/',include('user_account.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
