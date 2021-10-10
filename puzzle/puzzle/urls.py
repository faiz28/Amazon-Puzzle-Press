from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import homepage.views
from puzzle.upload import 

urlpatterns = [
    path('',homepage.views.home,name='home'),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
