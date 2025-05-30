from django.shortcuts import render
from django.http import JsonResponse
from bookapp.models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    print(books.values())
    data = {
        'books' : list(books.values())
    }
    return JsonResponse(data)

def book_details(request, id):
    book = Book.objects.get(id=id)
    print(book)
    data = {
        'title' : book.title,
        'author' : book.author,
        'isbn' : book.isbn
    }
    return JsonResponse(data)