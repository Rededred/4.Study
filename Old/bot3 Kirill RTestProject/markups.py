from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def user_menu_kb() -> InlineKeyboardMarkup:
    btn_top_up = InlineKeyboardButton(text='Пополнить', callback_data='top_up')
    top_up_menu = InlineKeyboardMarkup(row_width=1)
    top_up_menu.insert(btn_top_up)
    return top_up_menu


def buy_menu(is_url: bool = True, url: str = '', bill: int = None):
    qiwi_menu = InlineKeyboardMarkup(row_width=1)
    if is_url:
        btn_url_qiwi = InlineKeyboardButton(text='Ссылка на оплату', url=url)
        qiwi_menu.row(btn_url_qiwi)
    btn_check_qiwi = InlineKeyboardButton(text='Проверить оплату', callback_data=f'check_{bill}')
    qiwi_menu.row(btn_check_qiwi)
    return qiwi_menu
