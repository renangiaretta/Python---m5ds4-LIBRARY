from rest_framework import serializers


class BookMarkSerializer(serializers.Serializer):
    chapter = serializers.IntegerField()
    note = serializers.CharField()

    book_title = serializers.CharField(source='book.title', read_only=True)
    marker_username = serializers.CharField(source='marker.username', read_only=True)
