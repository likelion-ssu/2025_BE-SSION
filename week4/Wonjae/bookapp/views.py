from django.shortcuts import render
from django.http import JsonResponse
from bookapp.models import Book
from bookapp.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import APIView
from reviewapp.models import Review
from reviewapp.serializers import BookReviewSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookReviewList(APIView):
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
        book=Book.objects.get(id=id)
        if serializer.is_valid():
            serializer.save(
                book=book
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookReviewDetailsView(APIView):
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
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
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PATCH', 'DELETE'])
# def book_details(request,id):
#     if request.method == 'GET':
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return Response({'message':'도서를 찾지 못했습니다. '},status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return Response({'message':'도서를 찾지 못했습니다. '},status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return Response({'message':'도서를 찾지 못했습니다. '},status=status.HTTP_404_NOT_FOUND)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)