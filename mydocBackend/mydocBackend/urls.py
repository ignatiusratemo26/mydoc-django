from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import mydoc_api

router = routers.DefaultRouter()

urlpatterns = routers.urls

urlpatterns =+ [
    path('admin/', admin.site.urls),
    path('api/', include(mydoc_api.urls)),

]
