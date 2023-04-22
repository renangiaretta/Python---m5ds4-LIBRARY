from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    owner_id = serializers.IntegerField(read_only=True)
    book_owner = serializers.CharField(source='owner.username', read_only=True)

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
