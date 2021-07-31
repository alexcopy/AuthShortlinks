from django.contrib import admin
from .models import User, Post, Report

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Report)
# Register your models here.
