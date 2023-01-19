from django.db import models


class Book(models.Model):
    """
    Вот здесь описывается модель которая будет храниться в базе данных
    max_length - необходимый параметр для поля CharField иначе создать миграцию
    для нашей таблицы не получится (общее правило для всех хранимых в БД строк)

    параметры полей: null и blank
    null - если True то наше поле может быть пустым в БД
    blank - если True то наше поле при создании экземпляра класса можно не заполнять т.е.
    не обязательно к заполнению (так же отностися к админке, попробуй поменять с False на True)
    """
    title = models.CharField("Название", max_length=255, null=False, blank=False)
    numer_of_pages = models.PositiveIntegerField("Кол-во страниц", null=False, blank=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.author}"


class Author(models.Model):
    CHOICES_gander = (
        ('w', 'woman'),
        ('m', 'man'),
    )
    name = models.CharField("Имя", max_length=255, null=False, blank=False)
    surname = models.CharField("Фамилия", max_length=255, null=False, blank=False)
    patronymic = models.CharField("Отчество", max_length=255, null=False, blank=False)
    year_of_birth = models.DateField("Год рождения", auto_now=False, auto_now_add=False, null=False, blank=False)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    gander = models.CharField("Пол", max_length=255, null=False, blank=False, choices=CHOICES_gander)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} "


class Country(models.Model):
    name = models.CharField("Страна", max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Clothes(models.Model):
    CHOICES_season = (
        ('z','Зима'),
        ('l', 'Лето'),
        ('m', 'Демисезонная')
    )
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    color = models.CharField("Цвет", max_length=255, null=False, blank=False)
    season = models.CharField("Сезон", max_length=100, null=False, blank=False, choices=CHOICES_season)

    def __str__(self):
        return f"{self.type.name} | {self.color} | {self.get_season_display()}"


class Type(models.Model):
    name = models.CharField("Тип одежды", max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
