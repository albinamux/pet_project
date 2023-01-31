import pytest

from rest_framework.test import APIClient
from rest_framework import status

drf_client = APIClient()


class TestBook():
    @pytest.mark.django_db  # создаёт подключение к БД
    def test_get_book_list(self):
        response = drf_client.get('/api/books/')
        assert response.status_code == status.HTTP_200_OK
        # assert response.content == <obj>
