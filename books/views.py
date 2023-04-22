from rest_framework.views import APIView, Request, Response, status

from books.models import Book
from books.serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from accounts.permissions import IsAdminOrReadOnly
from .permissions import IsBookOwner
from django.shortcuts import get_object_or_404


class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class BookDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsBookOwner]

    def get(self, request: Request, book_id: int) -> Response:
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, book_id: int) -> Response:
        book = get_object_or_404(Book, pk=book_id)
        self.check_object_permissions(request, obj)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, book_id: int) -> Response:
        book = get_object_or_404(Book, pk=book_id)
        self.check_object_permissions(request, book)
        serializer = BookSerializer(
            instance=book,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
