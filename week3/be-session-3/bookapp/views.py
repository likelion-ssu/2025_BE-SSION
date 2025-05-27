from django.shortcuts import render
from django.http import JsonResponse
from bookapp.models import Book
# Create your views here.
def book_list(request):
    books = Book.objects.all()  
    print(books.values())
    data = {'books': list(books.values())}

    return JsonResponse(data)
    #이후return을 해야 화면에 출력된다

def book_details(request, id):
    book = Book.objects.get(id=id)
    print(book)
    data = {'title': book.title, 'author': book.author, 'isbn': book.isbn}
    #원하는 함수를 get을 통해서 id로 가져오겠다

    return JsonResponse(data)