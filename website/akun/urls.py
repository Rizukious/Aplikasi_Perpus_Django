from django.urls import path
from . import views

urlpatterns = [
    path('pendaftaran/', views.PendaftaranView.as_view(), name='Pendaftaran')
]
