from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status, APIView
from .serializers import BookMark
from books.models import Book
from book_marks.models import BookMarkSerializer


class BookMarkView(APIView):
    def get(self, request: Request, book_id: int) -> Response:
        book_obj = get_object_or_404(Book, pk=book_id)
        bookmarks = Bookmar(book=book_obj)
        serializer = BookMarkSerializer(bookmarks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
