from django.contrib import admin

# Register your models here.
from booklibrary.users.models import User

admin.site.register(User)