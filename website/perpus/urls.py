from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_buku, name="create_buku"),
    path('update/<int:id>', views.update_buku, name="create_buku"),
    path('delete/<int:id>', views.delete_buku, name="create_buku")
]
