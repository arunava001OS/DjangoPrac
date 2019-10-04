
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_blog/',include('admin_blog.urls')),
]
