from booklibrary.book.models import Book, Reviews
from booklibrary.book.filters import BookFilter



class SuggestService:

    @staticmethod
    def suggest_book_list(*, user, filters=None):
        reviews = Reviews.objects.filter(user=user)
        if reviews:
            filters = filters or {}
            user_reviews = Reviews.objects.filter(user=user).select_related('book')
            user_genres = user_reviews.values_list('book__genre', flat=True).distinct()

            books_in_genres = Book.objects.filter(genre__in=user_genres).exclude(
                book_reviews__user=user
            ).order_by('genre') # Books that the user has not rated yet and are in her favorite genre

            return BookFilter(filters, books_in_genres).qs
