import django_filters
from django.contrib.auth import get_user_model
User = get_user_model()



class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ("id", "username", "is_active")
