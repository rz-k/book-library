from booklibrary.book.models import Reviews
# from booklibrary.book.filters import BookFilter
from django.db import transaction



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

    # @transaction.atomic
    # @staticmethod
    # def media_update(*, media:Media, data) -> Media:
    #     non_side_effect_fields = ["name", "description", "file", "tags"]
    #     media, has_update = model_update(
    #         instance=media, 
    #         fields=non_side_effect_fields,
    #         data=data
    #     )            
    #     return media

    # @staticmethod
    # def file_write_disk(*, file, media_root_tmp="media"):
    #     storage = FileSystemStorage(location=media_root_tmp)
    #     file.name = storage.get_available_name(file)
    #     storage.save(file.name, File(file))
    #     file_path = os.path.join(media_root_tmp, file.name)
    #     file = {
    #         "file_path":file_path,
    #         "name":file.name
    #     }
    #     return file

    # @staticmethod
    # def media_list(*, filters=None) -> QuerySet[Media]:
    #     filters = filters or {}
    #     qs = Media.objects.all()
    #     return MediaFilter(filters, qs).qs
    


    # @staticmethod
    # def get_book(*, book_id: int)-> Book:
    #     return Book.objects.get(id=book_id)

    # @staticmethod
    # def book_list(*, filters=None):
    #     filters = filters or {}
    #     qs = Book.objects.all().prefetch_related("book_reviews")
    #     return BookFilter(filters, qs).qs
