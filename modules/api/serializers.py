from modules.core.models import Book, Author, Country, Clothes
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'numer_of_pages', 'author']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['surname', 'name', 'patronymic']


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class ClothesSerializer(ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['type', 'color', 'season']