from django.core.management.base import BaseCommand
from modules.core.models import Book
import csv
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Export books to CSV file'

    def handle(self, *args, **options):
        # logger.debug("Начинаю выгрузку книг в файл {}")
        with open('book.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["название", "автор"])
            books = Book.objects.all()
            # добавить сообщение о количестве книг которые будут записаны в файл уровень DEBUG
            logger.debug(f"В файл запишется {len(books)} книг.")
            for book in books:
                logger.debug("Пишу книгу: ")
                writer.writerow([book.title, book.author])
