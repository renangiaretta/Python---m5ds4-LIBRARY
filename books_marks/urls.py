from django.urls import path
from .views import BookMarkView


urlpatterns = [
    path('books/<int:book_id>/bookmarks/', BookMarkView.as_view())
]
