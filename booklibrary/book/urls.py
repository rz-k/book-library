from django.urls import path
from booklibrary.book.apis.book_apis import (
    BookListApi
)


app_name="book"
urlpatterns = [
    path('list/', BookListApi.as_view(),name="book-list"),
]
