from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from bookapp.models import Book
from bookapp.serializers import BookSerializer
from reviewapp.models import Review
from reviewapp.serializers import BookReviewSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
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
        serializer = BookSerializer(book, data=request.data)    
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
        return Response(status=status.HTTP_204_NO_CONTENT) #굳이 응답할 데이터가 없을 때 사용, 즉 return으로 응답할 data 존재 x

class BookReviewListView(APIView):
    def get(self, request, id):
        try:    
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        reviews = book.reviews.all()
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        serializer = BookReviewSerializer(data=request.data)
        book = Book.objects.get(id=id)
        if serializer.is_valid():
            serializer.save(
                book=book
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class BookReviewDetailsView(APIView):
    def get(self, request, id, review_id):
        try:
            review = Review.objects.get(id=review_id, book_id=id)
        except Review.DoesNotExist:
            return Response(
                {'message': '해당 도서에 대한 리뷰를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, id, review_id):
        try:
            review = Review.objects.get(id=review_id, book_id=id)
        except Review.DoesNotExist:
            return Response(
                {'message': '해당 도서에 대한 리뷰를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookReviewSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, review_id):
        try:
            review = Review.objects.get(id=review_id, book_id=id)
        except Review.DoesNotExist:
            return Response(
                {'message': '해당 도서에 대한 리뷰를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()  
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         #post는 정보를 만드는 과정이라, 추가 과정이 필요,,, 변환 등등
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)    
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     #포스트 시의 로직직

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_details(request, id):
#     if request.method == 'GET':
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist:
#             return Response({'message': '도서를 찾지 못했습니다.'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     #put은 모든 데이터를 덮어씀
#     elif request.method == 'PUT':
#         book = Book.objects.get(id=id)
#         #put 은 post와 다르게 book 이라는 수정할 객체를 같이 보내줘야함, 보내지않으면 post처리
#         serializer = BookSerializer(book, data=request.data)    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     elif request.method == 'PATCH':
#         book = Book.objects.get(id=id)
#         #put 은 post와 다르게 book 이라는 수정할 객체를 같이 보내줘야함, 보내지않으면 post처리
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