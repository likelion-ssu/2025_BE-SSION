from rest_framework import serializers
from reviewapp.models import Review
from bookapp.serializers import BookSerializer

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True) #책 내용 보여주는 거임 이거 주석처리하면 review만 딱 보여줌
    class Meta:
        model = Review
        fields = '__all__'