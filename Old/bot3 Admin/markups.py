from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Интерфейс пользователя
btnProfile = KeyboardButton('Мой профиль')
btnApplication = KeyboardButton('Оставить заявку')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile, btnApplication)

btnHead = KeyboardButton('Указать тему')
btnBody = KeyboardButton('Заявка')
applcationMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHead, btnBody)

# Интерфейс администратора
btnApplicationS = KeyboardButton('Заявки')

btnOkMan = KeyboardButton('Принять')
btnHastDoEinProblem = KeyboardButton('Отклонить')

btnUser = KeyboardButton('Меню пользователя')
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnApplicationS, btnUser)