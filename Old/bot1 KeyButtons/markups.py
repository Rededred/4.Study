from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Первое меню
btnA = KeyboardButton('Какое это меню?')
btnChangeOne = KeyboardButton('Поменять')
firstMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnA, btnChangeOne)


# Второе меню
btnC = KeyboardButton('А это какое?')
btnE = KeyboardButton('Остаться тут')
btnChangeTwo = KeyboardButton('Поменять обратно')
secondMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnC, btnE, btnChangeTwo)