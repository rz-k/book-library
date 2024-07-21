from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def rating_validator(rating):

    if not isinstance(rating, int):
        raise ValidationError(
            _("raiting must be integer"),
            code="raiting must be integer"
            )
    if rating < 1 or rating > 5:
        raise ValidationError(
            _("raiting must be number between 1-5"),
            code="raiting must be number between 1-5"
            )

