from rest_framework import routers
from modules.api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')  # добавлен в роуты
router.register(r'authors', views.AuthorViewSet)  # добавлен в роуты
router.register(r'countrys', views.CountryViewSet)
router.register(r'clothes', views.ClothesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
