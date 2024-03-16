# # import logging
# # from aiogram import Bot, Dispatcher, executor, types
# #
# import markups as ma
# #
# # bot = Bot(token=TOKEN)
# # dp = Dispatcher(bot)
# #
# #
# # @dp.message_handler(commands=['admin'], user_id=int(admin_id))
# # async def admin(mes: types.Message):
# #     pass
admins = set()
users = set()

class Admin(Filter):
    key = "is_admin"

    async def check(self, message: types.Message):
        return message.from_user.username in admins

class User(Filter):
    key = "is_user"

    async def check(self, message: types.Message):
        return message.from_user.username in users
# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Filter
# import markups as ma
# from config import TOKEN
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
# admins = set()
#
# @dp.message_handler(commands=['start'])
# async def command_start(message: types.Message):
#     await bot.send_message(message.from_user.id,'Привет,{0.first_name}!\nЯ рассмотрю твою заявку!'.format(message.from_user),reply_markup=ma.userMenu)
#
# @dp.message_handler(commands=['/admin'])
# async def bot_success(message: types.Message):
#     if message.from_user.id == '15':
#         admins.add_user(message.from_user.id)
#         await bot.send_message(message.from_user.id, 'Смена меню...', reply_markup=ma.adminMenu)
#     else:
#         await message.reply('Не знаю такого')
#
# @dp.message_handler() # пароль админа
# async def admin_password(message: types.Message):
#     if message.text =='1':
#         await bot.send_message(message.from_user.id, 'Смена меню...', reply_markup=ma.adminMenu)
#
#     # elif message.text == '123':
#     #     await bot.send_message(message.from_user.id, 'Смена меню...', reply_markup=ma.adminMenu)
#

# @dp.message_handler(commands="make")
# async def add_to_admins(message: types.Message):
#     # admins.add(message.from_user.username)
#     await message.reply(f"{admins}")
#
#
# @dp.message_handler(commands="/admin 123")
# async def add_to_admins(message: types.Message):
#     admins.add(message.from_user.username)
#
#
# @dp.message_handler(commands="/admins_list")
# async def show_admins_list(message: types.Message):
#     await message.reply(f"{admins}")
#
#
# if __name__ == "__main__":
#     # dp.bind_filter(Admin)
#     # dp.bind_filter(User)
#     executor.start_polling(dp, skip_updates=True)

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Filter
#
# admins = set()
#
# class Admin(Filter):
#     key = "is_admin"
#
#     async def check(self, message: types.Message):
#         return message.from_user.username in admins
#
# @dp.message_handler(commands="/admin 123")
# async def add_to_admins(message: types.Message):
#     admins.add(message.from_user.username)

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

@dp.message_handler()
async def admin_interface(message: types.Message):
    if db.admin_exists(message.from_user.id):
        if message.text == 'Заявки':
            pass
        elif message.text == 'Меню пользователя':
            await bot.send_message(message.from_user.id, 'Теперь вы снова пользователь', reply_markup=nav.userMenu)


@dp.message_handler()
async def user_interface(message: types.Message):
    async def user_form(message: types.Message):
        if db.user_exists(message.from_user.id):
            if message.text == 'Мой профиль':
                await bot.send_message(message.from_user.id, 'Ваш UserName: {0.first_name}'.format(message.from_user))
            elif message.text == 'Оставить заявку':
                await bot.send_message(message.from_user.id, 'Сначала укажите тему, затем напишите заявку',
                                       reply_markup=nav.applcationMenu)
                if message.text == 'Тема заявки':
                    await bot.send_message(message.from_user.id, 'sfv')

# @dp.callback_query_handler(text="add_new")
# async def theme(callback: types.CallbackQuery):
#     await bot.send_message(callback.from_user.id, "Укажите тему заявки")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

