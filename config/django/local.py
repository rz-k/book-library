from .base import *  # noqa

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INSTALLED_APPS += [
    'debug_toolbar'
]

STATIC_URL = "static/"