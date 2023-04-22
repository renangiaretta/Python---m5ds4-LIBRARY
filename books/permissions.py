from rest_framework import permissions
from rest_framework.views import Request, View
from books.models import Book


class IsBookOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Book) -> bool:
        # if obj.owner == request.user:
        #     return True
        # return False

        # if request.user.is_superuser:
        #     return True

        return request.user.is_superuser or obj.owner == request.user  # mesma coisa q os comentários de cima
