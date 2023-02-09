"""
Файл для настроек тестов заведения тестовых объектов
"""
import pytest
from modules.core.models import Author, Country, Book
from datetime import date

@pytest.fixture
def test_author():
    country = Country(name="Austia")
    country.save()

    author = Author.objects.create(
        surname="test",
        name="test",
        patronymic="test",
        year_of_birth=date(year=1950, month=5, day=1),
        gander="w",
        country=country,
    )
    author.save()

@pytest.fixture
def test_book(test_author):
    book = Book.objects.create(
        title="test",
        numer_of_pages=1,
        author=Author.objects.get(id=1)
    )
    book.save()
