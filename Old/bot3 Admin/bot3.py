import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes

import config as cfg
import markups as nav
from db import Database

logging.basicConfig(level=logging.INFO)

admins = set()

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')


@dp.message_handler(func=lambda message: message.chat.id not in admins, )
async def some(message: types.Message):
    await bot.send_message(message.chat.id, 'Вы не зарегистрированы')

# для пользователя -----------------------------------------------------------------------------
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # if message.chat.type == 'private':
    #     if not db.user_exists(message.from_user.id):
    #         db.add_user(message.from_user.id)
    await bot.send_message(message.from_user.id,
                           'Добрый день,{0.first_name}!\nЯ рассмотрю твою заявку!'.format(message.from_user),
                           reply_markup=nav.userMenu)


# для админа -----------------------------------------------------------------------------------
@dp.message_handler(commands=['admin'])
async def reg_admin(message: types.Message):
    # if (admins.includes(message.from_user.id):
    # if message.chat.type == 'private':
    #     if not db.admin_exists(message.from_user.id):
    #         db.add_user(message.from_user.id)
    #     else:
    await bot.send_message(message.from_user.id, "Теперь вы администратор,{0.first_name}!".format(message.from_user),
                           reply_markup=nav.adminMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
