from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Регистрация'))
    kb.add(KeyboardButton('Главная страница'))
    return kb

def main_line() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add('Отправить')

    return kb
def choose_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Геймер'), KeyboardButton('Пользователь'), KeyboardButton('Волонтер')).add(KeyboardButton('Зарегистрироваться на мероприятии'))
    return kb

def event_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Интенсив ПРАКТИС'), KeyboardButton('КОД ИБ + ПРАКТИС')).add(KeyboardButton('Ярмарка стартапов'))
    return kb

def games_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('CS:GO')).add(KeyboardButton('DOTA 2'))
    return kb

def cancle_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Вернуться обратно'))
    return kb
