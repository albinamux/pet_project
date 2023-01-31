import logging

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from modules.core.models import Book, Author, Country, Clothes, Type
from modules.api.serializers import BookSerializer, AuthorSerializer, CountrySerializer, ClothesSerializer


logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        logger.debug("Trying to get book list")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        logger.debug("Successfully got book list")
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        logger.debug("Trying to create book")
        request_data = request.data
        book = Book(
            title=request_data.get("title"),
            numer_of_pages=request_data.get("numer_of_pages"),
            author=Author.objects.get(id=request_data.get("author"))
        )
        book.save()
        serializer = BookSerializer(book)
        logger.debug(f"Successfully created book with {book.title=}")
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        logger.debug(f"Trying to retrieve book with id={pk}")
        book = Book.objects.filter(id=pk).first()
        if book is None:
            return Response(f"book with id={pk} doesn't exists", status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        logger.debug(f"Successfully retrieve book with id={pk}")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        logger.debug(f"Trying to destroy book with id={pk}")
        book_to_delete = Book.objects.filter(id=pk).first()
        if book_to_delete is None:
            return Response(f"book with id={pk} doesn't exists")

        book_to_delete.delete()
        logger.debug(f"Successfully destroy book with {book_to_delete.title}")
        return Response(f"book with id={pk} was deleted")

    def partial_update(self, request, pk=None):
        logger.debug(f"Trying partial update book with id={pk}")
        book_to_update = Book.objects.filter(id=pk).first()
        if book_to_update is None:
            return Response(f"book with id={pk} doesn't exists")

        serializer = BookSerializer(book_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.debug(f"Successfully partial update book with id={pk}")
        return Response(serializer.data)


class AuthorViewSet(viewsets.ViewSet):
    queryset = Author.objects.all()

    def list(self, request, *args, **kwargs):
        logger.debug("Trying to get author list")
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        logger.debug("Successfully got author list")
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        logger.debug(f"Trying to create author")
        request_data = request.data
        gander = request_data.get("gander")
        if gander not in Author.get_genders():
            return Response(f"Gender: {gander} no in {Author.get_genders()}", status=status.HTTP_400_BAD_REQUEST)

        author = Author(
            name=request_data.get("name"),
            surname=request_data.get("surname"),
            patronymic=request_data.get("patronymic"),
            year_of_birth=request_data.get("year_of_birth"),
            country=Country.objects.get(id=request_data.get("country")),
            gander=request_data.get("gander")
        )
        author.save()
        logger.debug(f"Successfully created author with {author.name=}")
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        logger.debug(f"Trying retrieve author with id={pk}")
        author = Author.objects.filter(id=pk).first()
        if author is None:
            return Response(f"author with id={pk} doesn't exists", status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author)
        logger.debug(f"Successfully retrieved author with id={pk}")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        logger.debug(f"Trying delete author with id={pk}")
        author_to_delete = Author.objects.filter(id=pk).first()
        if author_to_delete is None:
            return Response(f"author with id={pk} doesn't exists", status=status.HTTP_404_NOT_FOUND)

        author_to_delete.delite()
        logger.debug(f"Successfully deleted author with id={pk}")
        return Response(f"author with id={pk} was deleted")

    def partial_update(self, request, pk=None):
        logger.debug(f"Trying update author with id={pk}")
        author_to_update = Author.objects.filter(id=pk).first()
        if author_to_update is None:
            return Response(f"Author wiht id={pk} doesn't exists")
        serializer = AuthorSerializer(author_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.debug(f"Successfully update author with id={pk}")
        return Response(serializer.data)


class CountryViewSet(viewsets.ViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        logger.debug("Trying to get country list")
        books = Country.objects.all()
        serializer = CountrySerializer(books, many=True)
        logger.debug("Successfully got country list")
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        logger.debug(f"Trying to retrieve country with id={pk}")
        country = Country.objects.filter(id=pk).first()
        if country is None:
            return Response(f"Country with id={pk} doesn't exists")
        serializer = CountrySerializer(country)
        logger.debug(f"Successfully retrieved country with id={pk}")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        logger.debug(f"Trying delete country with id={pk}")
        country_to_delete = Country.objects.filter(id=pk).first()
        if country_to_delete is None:
            return Response(f"Country with id={pk} doesn't exists")
        country_to_delete.delete()
        logger.debug(f"Successfully deleted country with id={pk}")
        return Response(f"Successfully deleted country with id={pk}")

    def create(self, request, *args, **kwargs):

        request_data = request.data
        country=Country(
            name=request_data.get("name")
        )
        country.save()
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        country_to_update = Country.objects.filter(id=pk).first()
        if country_to_update is None:
            return Response(f"Country with id={pk} doesn't exists")
        serializer = CountrySerializer(country_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class ClothesViewSet(viewsets.ViewSet):
    queryset = Clothes.objects.all()

    def list(self, request, *args, **kwargs):
        logger.debug("Trying to get clothes list")
        books = Clothes.objects.all()
        serializer = ClothesSerializer(books, many=True)
        logger.debug("Successfully got clothes list")
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        clothes = Clothes.objects.filter(id=pk).first()
        if clothes is None:
            return Response(f"Clothes with id={pk} doesn't exists")
        serializer = CountrySerializer(clothes)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        clothes_to_delete = Clothes.objects.filter(id=pk).firs()
        if clothes_to_delete is None:
            return Response(f"Clothes with id={pk} doesn't exists")
        clothes_to_delete.delete()
        return Response(f"Successfully deleted clothes with id={pk}")

    def partial_update(self, request, pk=None):
        clothes_to_update = Clothes.objects.filter(id=pk).first()
        if clothes_to_update is None:
            return Response(f"Clothes with id={pk} doesn't exists")
        serializer = CountrySerializer(clothes_to_update, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request_data = request.data
        season = request_data.get("season")
        if season not in Clothes.get_season():
            return Response(f"Season: {season} no in {Clothes.get_season()}", status=status.HTTP_400_BAD_REQUEST)
        clothes = Clothes(
            type=Type.objects.get(id=request_data.get("type")),
            color=request_data.get("color"),
            season=request_data.get("season")
        )
        serializer = ClothesSerializer(clothes)
        serializer.save()
        return Response(serializer.data)















