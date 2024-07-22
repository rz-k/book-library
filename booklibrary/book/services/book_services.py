from booklibrary.book.models import Book
from booklibrary.book.filters import BookFilter


class BookService:

    @staticmethod
    def get_book(*, book_id: int)-> Book:
        return Book.objects.get(id=book_id)

    @staticmethod
    def book_list(*, filters=None):
        filters = filters or {}
        qs = Book.objects.all().prefetch_related("book_reviews")
        return BookFilter(filters, qs).qs
