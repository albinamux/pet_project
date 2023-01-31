from django.views import View
from django.http import HttpResponse
from http import HTTPStatus
from modules.core.models import Book, Author, Clothes, Type


class BookView(View):
    model = Book
    context_object_name = "books_list"
    """
    This view implements Book API
    """
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return HttpResponse(status=HTTPStatus.OK, content=books)



class AuthorView(View):
    """
    This view implements Author API
    """
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        return HttpResponse(status=HTTPStatus.OK, content=authors)


class ClothesView(View):
    def get(self, request, *args, **kwargs):
        clothes = Clothes.objects.all()
        return HttpResponse(status=HTTPStatus.OK, content=clothes)


class TypeView(View):
    def get(self):
        type = Type.objects.all()
        return HttpResponse(status=HTTPStatus.OK, content=type)