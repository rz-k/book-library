from rest_framework import serializers
from booklibrary.book.models import Reviews
from booklibrary.book.validators import rating_validator


class InputReviewSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    rating = serializers.IntegerField(
        validators = [rating_validator]
    )

class OutPutReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews 
        fields = '__all__'

class InputReviewDetailSerializer(serializers.Serializer):
    rating = serializers.IntegerField(
        validators = [rating_validator]
    )
