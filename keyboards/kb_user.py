from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Регистрация'))
    return kb

def choose_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Киберспортивная команда'), KeyboardButton('Волонтер')).add(KeyboardButton('Зарегистрироваться на мероприятии')).add(KeyboardButton('Хочу в команду'))
    return kb

def games_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('CS:GO')).add(KeyboardButton('DOTA 2'))
    return kb

def cancle_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Вернуться обратно'))
    return kb
