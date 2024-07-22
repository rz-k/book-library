from django.urls import path
from booklibrary.users.apis.user_apis import (
    RegisterApi
)


app_name="api"
urlpatterns = [
    path('register/', RegisterApi.as_view(),name="register"),
]
