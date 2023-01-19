from django.core.management.base import BaseCommand
from modules.core.models import Book
import csv


class Command(BaseCommand):
    help = 'Export books to CSV file'

    def handle(self, *args, **options):
        with open('book.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimeter=";")
            writer.writerow(["название", "автор"])
            books = Book.objects.all()
            for book in books:
                # print(book)
                writer.writerow([book.title, book.author])
