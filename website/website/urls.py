
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('perpus/', include('perpus.urls')),
    path('akun/', include('django.contrib.auth.urls')),
    path('akun/', include('akun.urls')),
    path('admin/', admin.site.urls),
]
