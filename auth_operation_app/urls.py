from django.contrib import admin
from django.urls import path
from auth_operation_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('home/', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)