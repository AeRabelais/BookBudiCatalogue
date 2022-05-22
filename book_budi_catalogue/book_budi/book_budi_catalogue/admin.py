from django.contrib import admin

from .models import Book, ComicBook, Journal, Shelf, Genre, MediumType, BookByAuthor

admin.site.register(Book)
admin.site.register(ComicBook)
admin.site.register(Journal)
admin.site.register(Shelf)
admin.site.register(Genre)
admin.site.register(MediumType)
admin.site.register(BookByAuthor)