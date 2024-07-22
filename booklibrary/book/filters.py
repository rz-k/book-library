import django_filters
from booklibrary.book.models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ("id", "genre")
