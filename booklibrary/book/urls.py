from django.urls import path
from booklibrary.book.apis.book_apis import BookListApi 
from booklibrary.book.apis.rewiev_apis import ReviewApi 


app_name="book"
urlpatterns = [
    path('book/list/', BookListApi.as_view(),name="book-list"),
    path('review/add', ReviewApi.as_view(),name="review-add-api"),
]
