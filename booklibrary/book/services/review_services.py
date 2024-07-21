from booklibrary.book.models import Reviews
from django.db import transaction
from booklibrary.common.services import model_update

class ReviewService:

    @staticmethod
    def get_review(*, review_id: int, **kwargs)-> Reviews:
        return Reviews.objects.get(pk=review_id, **kwargs)
        
    @staticmethod
    def get_user_book_review(*, book_id: int, user_id: int,):
        return Reviews.objects.filter(book_id=book_id, user_id=user_id)
    
    @staticmethod
    def review_create(*, user_id, **kwargs) -> Reviews:      
        review = Reviews.objects.create(
            user_id=user_id,
            **kwargs
        )
        return review

    @transaction.atomic
    @staticmethod
    def review_update(*, review:Reviews, data) -> Reviews:
        non_side_effect_fields = ["rating"]
        review_obj, has_update = model_update(
            instance=review, 
            fields=non_side_effect_fields,
            data=data
        )            
        return review_obj
