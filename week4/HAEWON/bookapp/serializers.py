from rest_framework import serializers
from bookapp.models import Book

class BookSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Book
        fields = "__all__"
        
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=200)
    # author = serializers.CharField(max_length=200)
    # isbn = serializers.IntegerField()
    # publication_date = serializers.DateField()

    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.isbn = validated_data.get('isbn', instance.isbn)
    #     instance.publication_date = validated_data.get('publication_date', instance.publication_date)
    #     instance.save()
    #     return instance