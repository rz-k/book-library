from rest_framework.response import Response
from rest_framework.views import APIView
from booklibrary.api.mixins import ApiAuthMixin
from rest_framework import status, exceptions
from drf_spectacular.utils import extend_schema
from booklibrary.book.services.review_services import ReviewService
from booklibrary.utils.pagination import LimitOffsetPagination
from rest_framework.request import Request
from booklibrary.book.models import Reviews
from booklibrary.book.serializers.review_serializers import (
    InputReviewSerializer, OutPutReviewSerializer, InputReviewDetailSerializer
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

@extend_schema(tags=['reviews'])
class ReviewDetailApi(ApiAuthMixin, APIView):

    @extend_schema(request=InputReviewDetailSerializer)
    def put(self, request: Request, review_id: int):

        serializer = InputReviewDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            review = ReviewService.get_review(review_id=review_id, user=request.user)
        except Reviews.DoesNotExist as e:
            raise exceptions.NotFound(
                {"message": "review with provided review_id does not exists."}
            )
        try:
            review = ReviewService.review_update(
                review=review,
                data=request.data
            )
        except Exception as e:
            raise exceptions.ValidationError(
                {"message": f"{e}"}
            )

        return Response(OutPutReviewSerializer(review).data, status=status.HTTP_200_OK)

    def delete(self, request: Request, review_id: int):
        try:
            review = ReviewService.get_review(review_id=review_id, user=request.user)
        except Reviews.DoesNotExist as e:
            raise exceptions.NotFound(
                {"message": "review with provided review_id does not exists."}
            )
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

