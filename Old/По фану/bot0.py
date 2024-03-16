
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5334416160:AAFjgJmayf0_Txo7nWmfms62BBXJ2ugvOf8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    этот handler(куратор) будет вызван, когда юзер отправит '/start' or '/help' команды
    """
    await message.reply("Привет!\nЯ бот первой попытки!\U0001F31A\nНадеюсь, меня уже научили общаться\n")


@dp.message_handler()
async def echo(message: types.Message):  # Эхо - значит отвечает
    # Старый способ:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# async def my_handler(message: types.Message):
#     bot = Bot.get_current()
#     user = types.User.get_current()
