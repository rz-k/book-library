from booklibrary.common.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.validators import MinValueValidator, MaxValueValidator



class Book(BaseModel):
    title = models.CharField(
        max_length=200, 
        unique=True,
        db_index=True
    )

    author = models.CharField(
        max_length=200
    )

    genre = models.CharField(
        max_length=50,
        db_index=True
    )

    def __str__(self) -> str:
        return self.title[:30]

class Reviews(BaseModel):

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name="book_reviews",
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_reviews",
    )

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self) -> str:
        return f"{self.rating}:{self.user.username}-{self.book.title[:10]}"