from django.db import transaction 
from booklibrary.users.models import User
from django.contrib.auth import get_user_model
from booklibrary.common.services import model_update
from booklibrary.users.filters import UserFilter


class UserService:

    @staticmethod
    def get_user(*, user_id: int)-> User:
        return get_user_model().objects.get(id=user_id)

    @staticmethod
    def user_create(*, username: str, password:str, **kwargs) -> User:
        return get_user_model().objects.create_user(
            username=username, password=password, **kwargs
        )

    @transaction.atomic
    @staticmethod
    def user_update(*, user:User, data):
        non_side_effect_fields = []
        user, has_update = model_update(
            instance=user, 
            fields=non_side_effect_fields,
            data=data
        )            
        return user

    @staticmethod
    def user_list(*, filters=None):
        filters = filters or {}
        qs = get_user_model().objects.all()
        return UserFilter(filters, qs).qs
