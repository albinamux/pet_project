import pytest

from rest_framework.test import APIClient
from rest_framework import status

drf_client = APIClient()


class TestBook:
    @pytest.mark.django_db  # создаёт подключение к БД
    def test_get_book_list(self):
        response = drf_client.get('/api/books/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db  # создаёт подключение к БД
    @pytest.mark.usefixtures("test_author")
    def test_create_book(self):
        book = {
            "title": "Книга",
            "numer_of_pages": 1,
            "author": 1
        }
        response = drf_client.post('/api/books/', data=book, format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    @pytest.mark.usefixtures("test_book")
    def test_retrive_book(self):
        response = drf_client.get('/api/books/1/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    @pytest.mark.usefixtures("test_book")
    def test_destroy_book(self):
        response = drf_client.delete('/api/books/1/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    @pytest.mark.usefixtures("test_book")
    def test_partial_update(self):
        book = {
            "title": "Книга",
            "numer_of_pages": 2,
            "author": 1
        }
        response = drf_client.patch('/api/books/1/', data=book, format='json')
        assert response.status_code == status.HTTP_200_OK





