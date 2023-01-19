from django.urls import path
from modules.core.views import BookView, AuthorView, ClothesView


urlpatterns = [
    path('books/', BookView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('clothes/', ClothesView.as_view()),
]
