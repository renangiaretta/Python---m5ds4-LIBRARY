from django.db import models

# 1:N - Accounts - BookMark
# 1:N - Book - BookMark

# Através de Account -> Book e BookMark
# Através de Book -> Account e BookMark
# Através de Bokmark -> Account e Book


class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()

    # Account -> Book (1:N)

    owner = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='books',
    )

    markers = models.ManyToManyField(
        'accounts.Account',
        through='books_marks.BookMark',
        related_name='marked_books',
    )

    def __repr__(self) -> str:
        return f'<Book [{self.id}] - {self.title}>'



