from django.contrib import admin
from .models import Books, Authors, Review


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn']
    search_fields = ['title', 'author']


admin.site.register(Books, BooksAdmin)


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    search_fields = ['full_name']


admin.site.register(Authors, AuthorsAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'comment', 'stars_given']


admin.site.register(Review, ReviewAdmin)
