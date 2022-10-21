from django.contrib import admin
from library.models import Author, Genre, Book, Bookinstance

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Bookinstance)