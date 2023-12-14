from django.contrib import admin

# Register your models here.

from .models import Post, Book

admin.site.register(Post)
admin.site.register(Book)
