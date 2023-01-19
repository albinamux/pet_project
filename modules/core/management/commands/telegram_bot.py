from django.core.management.base import BaseCommand
from aiogram import executor

from modules.core.telegram_bot.bot import dispatcher


class Command(BaseCommand):
    help = 'Что я делаю? '

    def handle(self, *args, **options):
        """
        Функция вызова запуска телеграм бота.
        """
        executor.start_polling(dispatcher, skip_updates=True)
