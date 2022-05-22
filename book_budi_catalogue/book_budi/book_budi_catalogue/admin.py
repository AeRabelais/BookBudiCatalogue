from django.contrib import admin

from .models import Book, ComicBook, Journal, Shelf, Genre, MediumType, Author, Illustrator

admin.site.register(Book)
admin.site.register(ComicBook)
admin.site.register(Journal)

admin.site.register(Author)
admin.site.register(Illustrator)

admin.site.register(Shelf)
admin.site.register(Genre)
admin.site.register(MediumType)

