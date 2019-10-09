from django.contrib import admin
from django.urls import path
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
