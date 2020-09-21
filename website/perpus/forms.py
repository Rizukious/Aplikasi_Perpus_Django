from django import forms
from .models import MyBook


class MyBookForms(forms.ModelForm):
    class Meta:
        model = MyBook
        fields = ['judul', 'pengarang', 'kota']
