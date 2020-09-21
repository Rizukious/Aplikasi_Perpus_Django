from django.db import models


class MyBook(models.Model):
    judul = models.CharField(max_length=200)
    pengarang = models.CharField(max_length=200)
    kota = models.CharField(max_length=200)
