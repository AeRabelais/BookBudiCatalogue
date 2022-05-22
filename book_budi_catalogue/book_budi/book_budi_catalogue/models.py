from codeop import CommandCompiler
from tkinter import CASCADE
from django.db import models
from datetime import datetime


class Author(models.Model):
    # Columns
    name = models.CharField(name="author_name", max_length=100, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = "author"

class Illustrator(models.Model):
    # Columns
    name = models.CharField(name="illustrator_name", max_length=100, null=False, blank=False, unique=True)
    class Meta:
        db_table = "illustrator"

class Genre(models.Model):
    # Columns
    name = models.CharField(name="genre_name", max_length=100, null=False, blank=False, unique=True)
    
    class Meta:
        db_table = "genre"

class MediumType(models.Model):
    # Columns
    name = models.CharField(name="genre_name", max_length=100, null=False, blank=False, unique=True)

    class Meta:
        db_table = "medium_type"

class OwnershipStatus(models.Model):
    # Choices
    STAT_OPTS = (
        ("00", "Don't Own, Don't Want"),
        ("01", "Don't Own, Want"),
        ("10", "Own, Don't Want"),
        ("11", "Own, Want")
    )

    # Columns
    status = models.CharField(name="status", max_length=2, choices=STAT_OPTS, blank=False)
    description = models.CharField(name="description", max_length=200, unique=True, blank=False)

    class Meta:
        db_table = "ownership_status"


# 1. Mediums

class Book(models.Model):
    # Keys
    book_type = models.ForeignKey(MediumType, models.SET_NULL, null=True)
    ownership_stat = models.ForeignKey(OwnershipStatus, models.SET_NULL, null=True)
    # Columns
    title = models.CharField(name="book_title", max_length=200, unique=True, blank=False)
    publication_yr = models.DateField(name="publication_year", unique=False, blank=True)
    rating = models.FloatField(name="rating", unique=False, blank=True)
    rental_stat = models.BooleanField(name="rental_status", blank=True)

    # Relationships
    authors = models.ManyToManyField(Author, through="BookByAuthor", related_name="book_by_author")
    genres = models.ManyToManyField(Genre, through="BookByGenre", related_name="book_by_genre")

    class Meta:
        db_table = "book"

class ComicBook(models.Model):
    # Keys
    comic_type = models.ForeignKey(MediumType, models.SET_NULL, null=True)
    ownership_stat = models.ForeignKey(OwnershipStatus, models.SET_NULL, null=True)

    # Columns
    title = models.CharField(name = "comic_title", max_length=200, unique=True, blank=False)
    publisher = models.CharField(name="publisher", max_length=100, unique=False, blank=False)
    protagonist = models.CharField(name="protagonist", max_length=100, unique=False, blank=True)
    entry_number = models.IntegerField(name="entry_number", unique=False, blank=True)
    publication_yr = models.DateField(name="publication_year", unique=False, blank=False)
    rating = models.FloatField(name="rating", unique=False, blank=True)
    rental_stat = models.BooleanField(name="rental_status", blank=True)

    # Relations
    authors = models.ManyToManyField(Author, through="ComicByAuthor", related_name="comic_by_author")
    illustrators = models.ManyToManyField(Illustrator, through="ComicByIllustrator", related_name="comic_by_illustrator")
    genres = models.ManyToManyField(Genre, through="ComicByGenre", related_name="comic_by_genre")
    class Meta:
        db_table = "comic_book"


class Journal(models.Model):
    # Keys
    journal_type = models.ForeignKey(MediumType, models.SET_NULL, null=True)

    # Columns
    journal_title = models.CharField(name = "journal_title", max_length=200, unique=True, blank=False)
    description = models.CharField(name="journal_description", max_length=200, unique=True, blank=True)
    date_added = models.DateTimeField(name="date_added", default=datetime.now())
    date_finished = models.DateTimeField(name="date_finished", blank=True)
    status_notes = models.CharField(name="status_notes", max_length=200, blank=True)

class Shelf(models.Model):
    # Columns
    name = models.CharField(name="shelf_name", max_length=200, null=False, blank=False, unique=True)
    description = models.CharField(name="description", max_length=200, null=False, blank=False, unique=True)
    
    # Relations
    books = models.ManyToManyField(Book, through="BookByShelf", related_name="book_by_shelf")
    comics = models.ManyToManyField(ComicBook, through="ComicByShelf", related_name="comic_by_shelf")

    class Meta:
        db_table = "shelf"

# ASSOCIATIONS

class BookByShelf(models.Model):
    # Keys
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "book_by_shelf"


class ComicByShelf(models.Model):
    # Keys
    comic = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "comic_by_shelf"


class BookByAuthor(models.Model):
    # Keys
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "book_by_author"


class ComicByAuthor(models.Model):
    # Keys
    comic = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "comic_by_author"

class ComicByIllustrator(models.Model):
    # Keys
    comic = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
    illustrator = models.ForeignKey(Illustrator, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "comic_by_illustrator"

class BookByGenre(models.Model):
    # Keys
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "book_by_genre"


class ComicByGenre(models.Model):
    # Keys
    comic = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    # Columns
    date_recorded = models.DateTimeField(name="date_recorded", auto_now_add=True)
    class Meta:
        db_table = "comic_by_genre"


