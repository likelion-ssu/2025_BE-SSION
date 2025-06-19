from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView

from rest_framework import status

from bookApp.models import Book
from bookApp.serializers import BookSerializer

from reviewApp.models import Review
from reviewApp.serializers import BookReviewSerializer


class BookListView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class BookDetailsView(APIView):
    def get(self,requset,id):
        try :
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)
        serializer =BookSerializer(book)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)       

    def patch(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)   
             
    def delete(self,requset,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class BookReviewListView(APIView):
    def get(self,request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)

        reviews = book.reviews.all()
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self,request,id):
        serializer = BookReviewSerializer(data=request.data)
        book = Book.objects.get(id=id)

        if serializer.is_valid():
            serializer.save(
                book = book
            )
            return Response(serializer.data)
        else:
            Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class BookReviewDetailsView(APIView):
    def get(self,request,id,review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 첵 없어요'},status.HTTP_404_NOT_FOUND)

        try:
            review = book.reviews.get(id=review_id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 리뷰 없어요'},status.HTTP_404_NOT_FOUND)

        serializer = BookReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self,request,id,review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 첵 없어요'},status.HTTP_404_NOT_FOUND)

        try:
            review = book.reviews.get(id=review_id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 리뷰 없어요'},status.HTTP_404_NOT_FOUND)

        serializer = BookReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    def delete(self,request,id,review_id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 첵 없어요'},status.HTTP_404_NOT_FOUND)

        try:
            review = book.reviews.get(id=review_id)
        except Book.DoesNotExist:
            return Response({'message' : '찾는 리뷰 없어요'},status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def book_list(request) :
#     if request.method == 'GET':        
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET','PUT','PATCH','DELETE'])
# def book_details(request, id) : 
#     if request.method == 'GET' :
#         try :
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return Response({'message' : '찾는 거 없어요'},status.HTTP_404_NOT_FOUND)
#         serializer =BookSerializer(book)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT' :
#         book = Book.objects.get(id=id)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'PATCH' :
#         book = Book.objects.get(id=id)
#         serializer = BookSerializer(book, data=request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     elif request.method == 'DELETE' :
#         book = Book.objects.get(id=id)
#         book.delete()
#         return Response(status.HTTP_204_NO_CONTENT)