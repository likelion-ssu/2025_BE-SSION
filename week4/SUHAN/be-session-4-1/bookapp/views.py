from django.shortcuts import render
from django.http import JsonResponse
from bookapp.models import Book
from rest_framework.response import Response
from bookapp.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import APIView
from reviewapp.models import Review
from reviewapp.serializers import BookReviewSerializer

# Create your views here.
# def book_list(request):
#     books = Book.objects.all()
#     print(books.values())
#     data = {
#         'books': list(books.values())
#     }
#     return JsonResponse(data)

# def book_details(request, id):
#     book = Book.objects.get(id=id)
#     data = {
#         'title': book.title,
#         'author': book.author,
#         'isbn': book.isbn
#     }
#     return JsonResponse(data)

# @api_view(['GET','POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PATCH', 'DELETE'])
# def book_details(request, id):
#     if request.method == 'GET':
#         book = Book.objects.get(id=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         book = Book.objects.get(id=id)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         book = Book.objects.get(id=id)
#         book.delete()
#         return Response()

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialzer = BookSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors, status.HTTP_400_BAD_REQUEST)
        
class BookDetailsView(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookReviewListView(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        reviews = book.reviews.all()
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        serializer = BookReviewSerializer(data=request.data)
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save(
                book=book
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookReviewDetailView(APIView):
    def get(self, request, id, review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            review = book.reviews.get(id=review_id)
        except Review.DoesNotExist:
            return Response({'message': '리뷰를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self, request, id, review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            review = book.reviews.get(id=review_id)
        except Review.DoesNotExist:
            return Response({'message': '리뷰를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookReviewSerializer(review, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id, review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            review = book.reviews.get(id=review_id)
        except Review.DoesNotExist:
            return Response({'message': '리뷰를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)