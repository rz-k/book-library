import datetime

from config.env import env

# For more settings
# Read everything from here - https://styria-digital.github.io/django-rest-framework-jwt/#additional-settings

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=36),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=999999),
}
