from django.urls import path
from booklibrary.book.apis.book_apis import BookListApi 
from booklibrary.book.apis.rewiev_apis import ReviewApi , ReviewDetailApi
from booklibrary.book.apis.suggest_api import SuggestApi



app_name="book"
urlpatterns = [
    path('book/list/', BookListApi.as_view(),name="book-list"),
    path('review/', ReviewApi.as_view(),name="review-add-api"),
    path('review/<int:review_id>', ReviewDetailApi.as_view(),name="review-ditail-api"),
    path('suggest/', SuggestApi.as_view(),name="suggest-api"),
]
