from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from booklibrary.api.mixins import ApiAuthMixin
from rest_framework import status, exceptions
from drf_spectacular.utils import extend_schema
from booklibrary.book.services.review_services import ReviewService
from booklibrary.utils.pagination import LimitOffsetPagination
from booklibrary.book.serializers.review_serializers import (
    InputReviewSerializer, OutPutReviewSerializer
)



@extend_schema(tags=['reviews'])
class ReviewApi(ApiAuthMixin, APIView, LimitOffsetPagination):

    @extend_schema(request=InputReviewSerializer, responses=OutPutReviewSerializer)
    def post(self, request, *args, **kwargs):
        serializer = InputReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_book_review = ReviewService().get_user_book_review(
            user_id=request.user.id, 
            book_id=request.data.get("book_id")
        )
        if user_book_review.exists():
            raise exceptions.ValidationError(
                {"message": f"You have rated this book"}
            )
        
        try:
            review = ReviewService.review_create(
                user_id=request.user.id,
                **request.data
            )
        except Exception as e:
            raise exceptions.ValidationError(
                {"message": f"{e}"}
            )

        return Response(OutPutReviewSerializer(review, ).data, status=status.HTTP_201_CREATED)

