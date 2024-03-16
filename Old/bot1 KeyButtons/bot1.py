import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as ma
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет,{0.first_name}!\n\U0001F31A\nЯ бот второй попытки!'.format(message.from_user), reply_markup=ma.firstMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Какое это меню?':
        await bot.send_message(message.from_user.id, 'Первое меню!'.format(message.from_user))
    elif message.text == 'Поменять':
        await bot.send_message(message.from_user.id, 'Смена меню...', reply_markup=ma.secondMenu)
    elif message.text == 'А это какое?':
        await bot.send_message(message.from_user.id, 'Второе меню!'.format(message.from_user))
    elif message.text == 'Остаться тут':
        await bot.send_message(message.from_user.id, 'Всё ещё тут?'.format(message.from_user))
    elif message.text == 'Поменять обратно':
        await bot.send_message(message.from_user.id, 'Смена меню...', reply_markup=ma.firstMenu)
    else:
        await message.reply('Не знаю такого')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)