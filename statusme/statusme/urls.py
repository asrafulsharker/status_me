
from django.contrib import admin
from django.urls import path
from api.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
]
