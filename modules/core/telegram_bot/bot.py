from django.conf import settings

import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

# Диспетчер
dispatcher = Dispatcher(bot=bot)


# Хэндлер на команду /start
@dispatcher.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dispatcher.message_handler(commands=["answer"])
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dispatcher.message_handler(commands=["reply"])
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')
