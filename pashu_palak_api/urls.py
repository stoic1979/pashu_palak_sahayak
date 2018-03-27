from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from api import views
# from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include('api.urls')),
]
