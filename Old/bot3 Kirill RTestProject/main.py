import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from pyqiwip2p import QiwiP2P

import config as cfg
import markups as nav
from db import Database


logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')
p2p = QiwiP2P(auth_key=cfg.QIWI_TOKEN)


@dp.message_handler(types.ChatType.PRIVATE, commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)

    await bot.send_message(message.from_user.id,
                           f'Ваш счет: {db.user_money(message.from_user.id)} рублей',
                           reply_markup=nav.user_menu_kb())


@dp.message_handler()
async def bot_mess(message: types.Message):
    if message.text.isdecimal() or message.text.isdigit():
        message_money = int(message.text)
        if message_money >= 3:
            comment = f'{message.from_user.id}_{random.randint(1000, 9999)}'
            bill = p2p.bill(amount=message_money, lifetime=15, comment=comment)

            db.add_check(message.from_user.id, message_money, bill.bill_id)

            await bot.send_message(message.from_user.id,
                                   f'Вы должны отправить {message_money} рублей на наш счет QIWI\n\n'
                                   f'Ссылка в кнопке или тут:{bill.pay_url}\n\n'
                                   f'Комментарий в форме оплаты должен быть следующим:{comment}',
                                   reply_markup=nav.buy_menu(url=bill.pay_url, bill=bill.bill_id))
            return 
        await bot.send_message(message.from_user.id, 'Минимальная сумма 3 рубля')
        return 
    await bot.send_message(message.from_user.id, 'Введите целое число')


@dp.callback_query_handler(text='top_up')
async def top_up(call: types.CallbackQuery):
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_message(call.from_user.id, 'Введите сумму')


@dp.callback_query_handler(text_contains='check_')
async def top_up(call: types.CallbackQuery):
    bill = call.data[6:]
    info = db.get_check(bill)
    if not info:
        if str(p2p.check(bill_id=bill).status) == 'PAID':
            user_money = db.user_money(call.from_user.id)
            money = int(info[2])
            db.set_money(call.from_user.id, user_money + money)
            await bot.send_message(call.from_user.id, 'Ваш счет пополнен! Напишите /start')
            db.delete_check(bill)
            return 
        await bot.send_message(call.from_user.id, 'Счёт ещё не оплачен!',
                               reply_markup=nav.buy_menu(False, bill=bill))
        return 
    await bot.send_message(call.from_user.id, 'Счет не найден')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
