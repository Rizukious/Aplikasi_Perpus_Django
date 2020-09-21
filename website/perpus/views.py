from django.shortcuts import render, redirect
from .forms import MyBookForms
from .models import MyBook


def create_buku(request):
    form = MyBookForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/perpus')
    return render(request, 'index.html', {'form': form, 'books': MyBook.objects.all()})


def update_buku(request, id):
    id = MyBook.objects.get(id=id)
    form = MyBookForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return redirect('/perpus')
    return render(request, 'index.html', {'form': form, 'books': MyBook.objects.all()})


def delete_buku(request, id):
    book = MyBook.objects.get(id=id)
    book.delete()
    return redirect('/perpus')
