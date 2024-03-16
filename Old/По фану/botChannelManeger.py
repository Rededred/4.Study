import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from conf import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['/test'])
async def cmd_test(message: Message):
    chat_id = 1515819727 # -1001515819727
    link = await bot.create_chat_invite_link(chat_id)
    await message.answer(message.link())

@dp.can_be_edited_handler(user_id=[""])
async def smth(message: Message):
    await bot.send_message(message.chat.id, message.text)
    await message.answer("Привет!")


async def check(self, message: types.Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.is_chat_admin() == self.is_admin


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)