from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Core
    path('', include('core.urls')),
    # Admin
    path('admin/', admin.site.urls),
]
