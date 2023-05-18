from aiogram import types, dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_user
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from lib import handler
import re 

START_TEXT = """
<b>Вас приветсвует Телеграм Бот PRACTICE</b>
Начиная работу с ботом, <b>ВЫ даете согалсие на обработку персональных данных</b>
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>"""

CANCLE_TEXT = """
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>
"""
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("bot\practice-386921-509b771b164d.json",scope)

client = gspread.authorize(creds)

GamerSheet = client.open("PracticeData").get_worksheet(0)
UserSheet = client.open("PracticeData").get_worksheet(1)
VolounteerSheet = client.open("PracticeData").get_worksheet(2)


class ClientStates(StatesGroup):
    person = State()
    fio = State()
    telephone = State()
    date_of_birthday = State()
    education = State()
    profession = State()
    email = State()
    subject = State()
    team_name = State()
    nickname = State()
    rating = State()
    steam = State()
    discord = State()
    event = State()

async def start_registration(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id, 
                        photo='https://i.imgur.com/o7sOfGx.png', 
                        caption=START_TEXT, 
                        parse_mode='HTML', 
                        reply_markup=kb_user.get_keyboard())

async def choose(message: types.Message) -> None:
    await message.reply(text="Выберите тип регистрации", 
                        reply_markup=kb_user.choose_keyboard())
    await ClientStates.person.set()

async def reg(message: types.Message) -> None:
    await message.reply(text="Нажмите кнопку 'Регистрация'", 
                        reply_markup=kb_user.get_keyboard())

async def cancle(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply(text=CANCLE_TEXT, reply_markup=kb_user.get_keyboard(), parse_mode='HTML')
    await state.finish()

async def get_person(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['person'] = message.text
    await ClientStates.next()
    await message.reply('Введите ваше ФИО', reply_markup=kb_user.cancle_keyboard())

async def get_fio(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await ClientStates.next() 
    await message.reply('Введите ваш телефон', reply_markup=kb_user.cancle_keyboard())

async def get_telephone(message: types.Message, state: FSMContext) -> None:
    phone = await handler.is_int_phone(message.text)
    if phone == True:
        async with state.proxy() as data:
            data['telephone'] = message.text
        await ClientStates.next() 
        await message.reply('Введите вашу дату рождения.\n<b>Формат: DD.MM.YYYY</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')
    else:
        await message.reply('Неверный ввод')

async def get_date_of_birthday(message: types.Message, state: FSMContext) -> None:
    date = await handler.is_valid_date(message.text)
    if date == True:
        async with state.proxy() as data:
            data['date_of_birthday'] = message.text
        await ClientStates.next() 
        await message.reply('Введите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())
    else:
        await message.reply('Неверный ввод.\n<b>Формат: DD.MM.YYYY</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_education(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    await ClientStates.next() 
    await message.reply('Введите вашу специальность', reply_markup=kb_user.cancle_keyboard())

async def get_profession(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await ClientStates.next() 
    await message.reply('Введите ваш email.\n<b>Формат: practice@gmail.com</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_email(message: types.Message, state: FSMContext) -> None:
    check = await handler.is_valid_email(message.text)
    if check == True:
        async with state.proxy() as data:
            data['email'] = message.text
            
    else:
        await message.reply('Неверный ввод.\n<b>Формат: practice@gmail.com</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')
    if data['person'] != 'Геймер':
        
        
        await bot.send_message(chat_id=message.from_user.id,
                                text=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")
        await message.answer('Ваши данные сохранены', reply_markup=kb_user.cancle_keyboard())

        df = [data["person"],
                       
                         data['fio'],
                         data['telephone'],
                         data['date_of_birthday'],
                         data['education'],
                        data['email'],
                         data['profession']]
        
        if data["person"] == "Пользователь":
            UserSheet.insert_row(df)
        else:
            
            VolounteerSheet.insert_row(df)
        
        await state.finish()
    else:
        await ClientStates.next()  
        await message.reply(text='Выберите дисциплину', reply_markup=kb_user.games_keyboard())

async def get_subject(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['subject'] = message.text
    await ClientStates.next()
    await message.reply('Напишите наименование команды', reply_markup=kb_user.cancle_keyboard())

async def get_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['team_name'] = message.text
    await ClientStates.next()
    await message.reply('Напишите ваш никнейм в игре', reply_markup=kb_user.cancle_keyboard())

async def get_nickname(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['nickname'] = message.text
    await ClientStates.next() 
    await message.reply('Введите ваш рейтинг в игре', reply_markup=kb_user.cancle_keyboard())

async def get_rating(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['rating'] = message.text
    await ClientStates.next() 
    await message.reply('Отправьте ссылку на ваш профиль steam.\n<b>Формат: httрs://steamcommunity.com/id/<u>"ваш steam-id"</u>/</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_steam(message: types.Message, state: FSMContext) -> None:
    steam = await handler.is_steam_link(message.text)
    if steam == True:
        async with state.proxy() as data:
            data['steam'] = message.text
        await ClientStates.next() 
        await message.reply('Отправьте ваш дискорд.\n<b>Формат: practice#1234</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')
    else:
        await message.reply('Неверный ввод.\n<b>Формат: httрs://steamcommunity.com/id/<u>"ваш steam-id"</u>/</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_discord(message: types.Message, state: FSMContext) -> None:
    discord = await handler.is_valid_discord(message.text)
    if discord == True:
        async with state.proxy() as data:
            data['discord'] = message.text
        
        await bot.send_message(chat_id=message.from_user.id, 
                            text=f"Название команды: {data['team_name']}\nДисциплина: {data['subject']}\nУчебное заведение: {data['education']}\nФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nНикнейм: {data['nickname']}\nРейтинг: {data['rating']}\nSteam: {data['steam']}\nDiscord: {data['discord']}\nСпециальность: {data['profession']}")

        df = ["Геймер",
                       data['team_name'],
                        data['subject'],
                        data['education'],
                         data['fio'],
                         data['telephone'],
                         data['date_of_birthday'],
                         data['nickname'],
                        data['rating'],
                        data['steam'],
                         data['discord'],
                         data['profession']]
        GamerSheet.insert_row(df)
        await message.answer('Ваши данные сохранены', reply_markup=kb_user.cancle_keyboard())
        await state.finish()
    else:
        await message.reply('Неверный ввод.\n<b>Формат: practice#1234</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# async def choose_events(message: types.Message):
#     await message.reply(text="Выберите мероприятие", 
#                         reply_markup=kb_user.event_keyboard())
#     await ClientStates.event.set()

# async def events(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['event'] = message.text
#     await state.finish()
#     await message.reply(f"Вы успешно зарегистрированы на мероприятие: {data['event']}", reply_markup=kb_user.cancle_keyboard())
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# @dp.message_handler(lambda message: not message.photo, state=VolunteerStates.student_ID_card)
# async def check_photo_studV(message: types.Message):
#     return await message.reply('Это не фотография!')

# @dp.message_handler(lambda message: message.photo, content_types=['photo'], state=VolunteerStates.photo)
# async def get_photoV(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await message.answer('Ваши данные сохранены')

#     async with state.proxy() as data:
#         await bot.send_photo(chat_id=message.from_user.id,
#                             photo=data['photo'],
#                             caption=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")

#     state.finish()

def register_handlers_user(dp: dispatcher):
    dp.register_message_handler(start_registration, commands=["start"])
    dp.register_message_handler(choose, Text(equals='Регистрация'))
    dp.register_message_handler(cancle, Text(equals='Вернуться обратно'), state='*')
    # dp.register_message_handler(choose_events, Text(equals='Зарегистрироваться на мероприятии'))
    # dp.register_message_handler(events, Text(['Интенсив ПРАКТИС', 'КОД ИБ + ПРАКТИС', 'Ярмарка стартапов']), state=ClientStates.event)
    dp.register_message_handler(get_person, Text(['Геймер', 'Пользователь', 'Волонтер']), state=ClientStates.person)
    dp.register_message_handler(get_fio, state=ClientStates.fio)
    dp.register_message_handler(get_telephone, state=ClientStates.telephone)
    dp.register_message_handler(get_date_of_birthday, state=ClientStates.date_of_birthday)
    dp.register_message_handler(get_education, state=ClientStates.education)
    dp.register_message_handler(get_profession, state=ClientStates.profession)
    dp.register_message_handler(get_email, state=ClientStates.email)
    dp.register_message_handler(get_subject, Text(['CS:GO', 'DOTA 2']), state=ClientStates.subject)
    dp.register_message_handler(get_team, state=ClientStates.team_name)
    dp.register_message_handler(get_nickname, state=ClientStates.nickname)
    dp.register_message_handler(get_rating, state=ClientStates.rating)
    dp.register_message_handler(get_steam, state=ClientStates.steam)
    dp.register_message_handler(get_discord, state=ClientStates.discord)

        # dp.register_message_handler(check_photo, lambda message: not message.photo, state=ClientStates.photo)
        # dp.register_message_handler(get_photo, lambda message: message.photo, content_types=['photo'], state=ClientStates.photo)
        # dp.register_message_handler(check_photo_cap, lambda message: not message.photo, state=ClientStates.photo_cap)
        # dp.register_message_handler(get_photo_cap, lambda message: message.photo, content_types=['photo'], state=ClientStates.photo_cap)
        # dp.register_message_handler(check_photo_stud, lambda message: not message.photo, state=ClientStates.student_ID_card)
        # dp.register_message_handler(get_student_ID_card, lambda message: message.photo, content_types=['photo'], state=ClientStates.student_ID_card)

    

