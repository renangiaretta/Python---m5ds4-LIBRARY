from django.db import models


class BookMark(models.Model):
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        related_name='book_marks'
        )

    markers = models.ForeignKey(
        'accounts.account',
        on_delete=models.CASCADE,
        related_name='user_book_marks',
        )

    chapter = models.IntegerField()
    note = models.TextField()

    def __repr__(self) -> str:
        return f'<BookMark [{self.id}] - {self.note}>'