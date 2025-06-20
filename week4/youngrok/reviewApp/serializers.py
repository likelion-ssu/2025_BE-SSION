from rest_framework import serializers
from reviewApp.models import Review
from bookApp.serializers import BookSerializer

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"