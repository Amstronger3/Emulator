from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.
from .models import Profile

admin.site.register(Profile)

# admin.site.unregister(User)
admin.site.unregister(Group)
