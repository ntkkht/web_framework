from django.shortcuts import render

# Create your views here.
from .models import Book

def homepage(request):
    book = Book.objects.values()
    return render(request, 'home.html', { 'books': book })