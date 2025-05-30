from django.shortcuts import render
from django.http import JsonResponse
from bookapp.models import Book

# Create your views here.

def showBook(request):
    books = Book.objects.all()
    print(books.values())
    data = {
        'book' : list(books.values())
    }
    return JsonResponse(data)

def showDetail(request,id):
    book = Book.objects.get(id=id)
    print(book)
    data = {
        'title' : book.title,
        'author' : book.author, 
        'isbn' : book.isbn,
    }
    return JsonResponse(data)
