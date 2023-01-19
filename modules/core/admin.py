from django.contrib import admin
from .models import Book, Author, Country, Clothes, Type


"""
@admin - это декоратор, который позволяет регистрировать модели
"""


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
