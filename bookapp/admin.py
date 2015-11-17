from django.contrib import admin
from bookapp.models import *
# coding=utf-8
# Register your models here.
class AuthorInline(admin.TabularInline):
    model = Author
    extra = 3


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ISBN']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['price']}),
        (None,               {'fields': ['publisher']}),
        (None,               {'fields': ['pubdate']}),
    ]
    inlines = [AuthorInline]
    list_display = ('ISBN','title','author','price','publisher','pubdate')


admin.site.register(Author)
admin.site.register(Book)