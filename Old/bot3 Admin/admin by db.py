import logging

from aiogram import Bot, Dispatcher, executor, types


import config as cfg
import markups as nav
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)

db = Database("database.db")


@dp.message_handler(commands=['start'])  # здоровается и добавляет пользователя в БД
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)

        await bot.send_message(message.from_user.id, 'Добрый день! Тут вы можете оставить свою заявку)',
                               reply_markup=nav.userMenu)

@dp.message_handler(commands=['admin'])# открывает меню администратора (или добавляет пользователя в список возможных админов)
async def admin(message: types.Message):
    if message.chat.type == 'private':
        if db.admin_exists(message.from_user.id):
            await bot.send_message(message.from_user.id, 'Вы в меню Администратора!', reply_markup=nav.adminMenu)
        elif not db.admin_exists(message.from_user.id):
            db.add_admin(message.from_user.id)
            await bot.send_message(message.from_user.id, "Введите пароль доступа:")


@dp.message_handler(text=['123']) # пароль для доступа к админке
async def proof_admin(message: types.Message):
    if db.admin_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Вы в меню Администратора!'.format(message.from_user), reply_markup=nav.adminMenu)
    else:
        pass


@dp.message_handler() # интерфейс пользователя
async def user_form(message: types.Message):
    if db.user_exists(message.from_user.id):
        if message.text == 'Мой профиль':
            await bot.send_message(message.from_user.id, 'Ваш UserName: {0.first_name}'.format(message.from_user))
        elif message.text == 'Оставить заявку':
            await bot.send_message(message.from_user.id, 'Cначала укажите тему, затем напишите заявку', reply_markup=nav.applcationMenu)
        elif message.text == 'Указать тему':
            db.add_theme(next(message.from_user.id), message.text)


# @dp.callback_query_handler(text="add_new")
# async def theme(callback: types.CallbackQuery):
#     await bot.send_message(callback.from_user.id, "Укажите тему заявки")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

