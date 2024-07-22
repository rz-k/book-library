from django.urls import path, include

urlpatterns = [
    path('users/', include(('booklibrary.users.urls', 'users'))),
    path('authentication/', include(('booklibrary.authentication.urls', 'authentication'))),
    path('', include(('booklibrary.book.urls', 'book'))),
]
