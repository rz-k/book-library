from rest_framework import serializers
from booklibrary.book.models import Reviews, Book


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews 
        fields = ('id', 'rating')

class OutPutBookSerializer(serializers.ModelSerializer):
    your_review = serializers.SerializerMethodField()
    class Meta:
        model = Book 
        fields = '__all__'

    def get_your_review(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            user_review = obj.book_reviews.filter(user=request.user).first()
            if user_review:
                return BookReviewSerializer(user_review).data
        return None

class BookFilterSerializer(serializers.Serializer):
    genre = serializers.CharField(
        required=False, allow_null=True, default=None
    )
