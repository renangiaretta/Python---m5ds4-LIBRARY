from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    published_date = serializers.DateTimeField()

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)
