from aiogram import types, dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_user

START_TEXT = """
<b>Вас приветсвует Телеграм Бот PRACTICE</b>
Начиная работу с ботом, <b>ВЫ даете согалсие на обработку персональных данных</b>
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>"""

CANCLE_TEXT = """
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>
"""

class ClientStates(StatesGroup):
    subject = State()
    team_name = State()
    education = State()
    # photo = State()
    # photo_cap = State()
    fio = State()
    telephone = State()
    date_of_birthday = State()
    nickname = State()
    rating = State()
    steam = State()
    discord = State()
    profession = State()
    # student_ID_card = State()
    
class VolunteerStates(StatesGroup):
    fio = State()
    telephone = State()
    date_of_birthday = State()
    education = State()
    profession = State()
    email = State()
    # photo = State()

class ToTeamStates(StatesGroup):
    fio = State()
    telephone = State()
    date_of_birthday = State()
    education = State()
    profession = State()
    email = State()
    # photo = State()

class EventStates(StatesGroup):
    fio = State()
    telephone = State()
    date_of_birthday = State()
    education = State()
    profession = State()
    email = State()
    # photo = State()

# @dp.message_handler(commands=["start"])
async def start_registration(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id, 
                        photo='https://i.imgur.com/o7sOfGx.png', 
                        caption=START_TEXT, 
                        parse_mode='HTML', 
                        reply_markup=kb_user.get_keyboard())

# @dp.message_handler(Text(equals='Регистрация'))
async def choose(message: types.Message) -> None:
    await message.reply(text="Выберите тип регистрации", 
                        reply_markup=kb_user.choose_keyboard())

# @dp.message_handler(Text(equals='В меню'))
async def reg(message: types.Message) -> None:
    await message.reply(text="Нажмите кнопку 'Регистрация'", 
                        reply_markup=kb_user.get_keyboard())
# Киберспортивная команда

# @dp.message_handler(Text(equals='Киберспортивная команда'))
async def cyber(message: types.Message) -> None:
    await message.reply(text='Выберите дисциплину', reply_markup=kb_user.games_keyboard())
    await ClientStates.subject.set()

# @dp.message_handler(Text(equals='Отмена'), state='*')
async def cancle(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await message.reply(text=CANCLE_TEXT, reply_markup=kb_user.get_keyboard(), parse_mode='HTML')
    await state.finish()

# @dp.message_handler(Text(['CS:GO', 'DOTA 2']), state=ClientStates.subject)
async def get_subject(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['subject'] = message.text
    await ClientStates.next()
    await message.reply('Напишите наименование комнады', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.team_name)
async def get_team_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['team_name'] = message.text
    
    await ClientStates.next()
    await message.reply('Введите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())


# @dp.message_handler(state=ClientStates.education)
async def get_education(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    
    await ClientStates.next()
    await message.reply('Введите ваше ФИО', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(lambda message: not message.photo, state=ClientStates.photo)
# async def check_photo(message: types.Message):
#     return await message.reply('Это не фотография!')

# @dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStates.photo)
# async def get_photo(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await ClientStates.next()                
#     await message.reply('Отправтье фото капитана команды', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(lambda message: not message.photo, state=ClientStates.photo_cap)
# async def check_photo_cap(message: types.Message):
#     return await message.reply('Это не фотография!')

# @dp.message_handler(lambda message: message.photo, content_types=['photo_cap'], state=ClientStates.photo_cap)
# async def get_photo_cap(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['photo_cap'] = message.photo[0].file_id
                    
#     await ClientStates.next()   
#     await message.answer(text='Введите ФИО', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.fio)
async def get_fio(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await ClientStates.next() 
    await message.reply('Напишите свой номер телефона', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.telephone)
async def get_telephone(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['telephone'] = message.text
    await ClientStates.next() 
    await message.reply('Напишите вашу дату рождения', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.date_of_birthday)
async def get_date_of_birthday(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['date_of_birthday'] = message.text
    await ClientStates.next() 
    await message.reply('Напишите свой игровой никнейм', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.nickname)
async def get_nickname(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['nickname'] = message.text
    await ClientStates.next() 
    await message.reply('Напишите свой рейтинг в игре', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.rating)
async def get_rating(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['rating'] = message.text
    await ClientStates.next() 
    await message.reply('Отправьте ссылку на ваш профиль steam', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.steam)
async def get_steam(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['steam'] = message.text
    await ClientStates.next() 
    await message.reply('Отправьте ваш дискорд (пример: practice#1234)', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.discord)
async def get_discord(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['discord'] = message.text
    await ClientStates.next() 
    await message.reply('Напишите вашу специальность', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ClientStates.profession)
async def get_profession(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await message.answer('Ваши данные сохранены')
    await bot.send_message(chat_id=message.from_user.id, 
                        text=f"Название команды: {data['team_name']}\nДисциплина: {data['subject']}\nУчебное заведение: {data['education']}\nФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nНикнейм: {data['nickname']}\nРейтинг: {data['rating']}\nSteam: {data['steam']}\nDiscord: {data['discord']}\nСпециальность: {data['profession']}")

    state.finish()
# @dp.message_handler(lambda message: not message.photo, state=ClientStates.student_ID_card)
# async def check_photo_stud(message: types.Message):
#     return await message.reply('Это не фотография!')

# @dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStates.student_ID_card)
# async def get_student_ID_card(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['student_ID_card'] = message.photo[0].file_id

    # await message.answer('Ваши данные сохранены')
    # async with state.proxy() as data:
    #     photos = types.MediaGroup()
    #     photos.attach_photo(photo=data['photo'])
    #     photos.attach_photo(photo=data['photo_cap'])
    #     photos.attach_photo(photo=data['student_ID_card'])
    #     await bot.send_media_group(chat_id=message.from_user.id, 
    #                         media=photos)
    #     await bot.send_message(chat_id=message.from_user.id, 
    #                         text=f"Название команды: {data['team_name']}\nДисциплина: {data['subject']}\nУчебное заведение: {data['education']}\nФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения {data['date_of_birthday']}\nНикнейм: {data['nickname']}\nРейтинг: {data['rating']}\nSteam: {data['steam']}\nDiscord: {data['discord']}\nСпециальность: {data['profession']}")

    #     state.finish()

# Волонтер

# @dp.message_handler(Text(equals='Волонтер'))
async def volunteer(message: types.Message) -> None:
    await message.reply(text='Введите ваши ФИО', reply_markup=kb_user.cancle_keyboard())
    await VolunteerStates.fio.set()

# @dp.message_handler(state=VolunteerStates.fio)
async def get_fioV(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await VolunteerStates.next() 
    await message.reply('Напишите ваш телефон', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=VolunteerStates.telephone)
async def get_telephoneV(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['telephone'] = message.text
    await VolunteerStates.next() 
    await message.reply('Напишите вашу дату рождения', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=VolunteerStates.date_of_birthday)
async def get_date_of_birthdayV(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['date_of_birthday'] = message.text
    await VolunteerStates.next() 
    await message.reply('Напишите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=VolunteerStates.education)
async def get_educationV(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    await VolunteerStates.next() 
    await message.reply('Напишите свою специальность', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=VolunteerStates.profession)
async def get_professionV(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await VolunteerStates.next() 
    await message.reply('Напишите свой email', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=VolunteerStates.email)
async def get_email(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['email'] = message.text
    async with state.proxy() as data:
        await bot.send_message(chat_id=message.from_user.id,
                            text=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")
    state.finish()
    await message.answer('Ваши данные сохранены', reply_markup=kb_user.cancle_keyboard())

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

# Хочу в команду

# @dp.message_handler(Text(equals='Хочу в команду'))
async def to_team(message: types.Message) -> None:
    await message.reply(text='Введите ваши ФИО', reply_markup=kb_user.cancle_keyboard())
    await ToTeamStates.fio.set()

# @dp.message_handler(state=ToTeamStates.fio)
async def get_fio_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await ToTeamStates.next() 
    await message.reply('Напишите ваш телефон', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ToTeamStates.telephone)
async def get_telephone_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['telephone'] = message.text
    await ToTeamStates.next() 
    await message.reply('Напишите вашу дату рождения', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ToTeamStates.date_of_birthday)
async def get_date_of_birthday_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['date_of_birthday'] = message.text
    await ToTeamStates.next() 
    await message.reply('Напишите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ToTeamStates.education)
async def get_education_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    await ToTeamStates.next() 
    await message.reply('Напишите свою специальность', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ToTeamStates.profession)
async def get_profession_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await ToTeamStates.next() 
    await message.reply('Напишите свой email', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=ToTeamStates.email)
async def get_email_team(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer('Ваши данные сохранены')
    async with state.proxy() as data:
            await bot.send_message(chat_id=message.from_user.id,
                                text=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")

    state.finish()

# @dp.message_handler(lambda message: not message.photo, state=ToTeamStates.photo)
# async def check_photo_team(message: types.Message):
#     return await message.reply('Это не фотография!')

# @dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ToTeamStates.photo)
# async def get_photo_team(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await message.answer('Ваши данные сохранены')

#     async with state.proxy() as data:
#         await bot.send_photo(chat_id=message.from_user.id,
#                             photo=data['photo'],
#                             caption=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")

#     state.finish()

#Мероприятие
# @dp.message_handler(Text(equals='Зарегистрироваться на мероприятии'))
async def event(message: types.Message) -> None:
    await message.reply(text='Введите ваши ФИО', reply_markup=kb_user.cancle_keyboard())
    await EventStates.fio.set()

# @dp.message_handler(state=EventStates.fio)
async def get_fio_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await EventStates.next() 
    await message.reply('Напишите ваш телефон', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=EventStates.telephone)
async def get_telephone_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['telephone'] = message.text
    await EventStates.next() 
    await message.reply('Напишите вашу дату рождения', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=EventStates.date_of_birthday)
async def get_date_of_birthday_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['date_of_birthday'] = message.text
    await EventStates.next() 
    await message.reply('Напишите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=EventStates.education)
async def get_education_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    await EventStates.next() 
    await message.reply('Напишите свою специальность', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=EventStates.profession)
async def get_profession_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await EventStates.next() 
    await message.reply('Напишите свой email', reply_markup=kb_user.cancle_keyboard())

# @dp.message_handler(state=EventStates.email)
async def get_email_event(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer('Ваши данные сохранены')
    async with state.proxy() as data:
        await bot.send_message(chat_id=message.from_user.id,
                            text=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")

    state.finish()


def register_handlers_user(dp: dispatcher):
    dp.register_message_handler(start_registration, commands=["start"])
    dp.register_message_handler(choose, Text(equals='Регистрация'))
    dp.register_message_handler(cancle, Text(equals='Вернуться обратно'), state='*')
    #Киберспортивная команда
    dp.register_message_handler(cyber, Text(equals='Киберспортивная команда'))
    dp.register_message_handler(get_subject, Text(['CS:GO', 'DOTA 2']), state=ClientStates.subject)
    dp.register_message_handler(get_team_name, state=ClientStates.team_name)
    dp.register_message_handler(get_education, state=ClientStates.education)
        #dp.register_message_handler(check_photo, lambda message: not message.photo, state=ClientStates.photo)
        #dp.register_message_handler(get_photo, lambda message: message.photo, content_types=['photo'], state=ClientStates.photo)
        #dp.register_message_handler(check_photo_cap, lambda message: not message.photo, state=ClientStates.photo_cap)
        #dp.register_message_handler(get_photo_cap, lambda message: message.photo, content_types=['photo'], state=ClientStates.photo_cap)
    dp.register_message_handler(get_fio, state=ClientStates.fio)
    dp.register_message_handler(get_telephone, state=ClientStates.telephone)
    dp.register_message_handler(get_date_of_birthday, state=ClientStates.date_of_birthday)
    dp.register_message_handler(get_nickname, state=ClientStates.nickname)
    dp.register_message_handler(get_rating, state=ClientStates.rating)
    dp.register_message_handler(get_steam, state=ClientStates.steam)
    dp.register_message_handler(get_discord, state=ClientStates.discord)
    dp.register_message_handler(get_profession, state=ClientStates.profession)
        #dp.register_message_handler(check_photo_stud, lambda message: not message.photo, state=ClientStates.student_ID_card)
        #dp.register_message_handler(get_student_ID_card, lambda message: message.photo, content_types=['photo'], state=ClientStates.student_ID_card)
    #Волонтер
    dp.register_message_handler(volunteer, Text(equals='Волонтер'))
    dp.register_message_handler(get_fioV, state=VolunteerStates.fio)
    dp.register_message_handler(get_telephoneV, state=VolunteerStates.telephone)
    dp.register_message_handler(get_date_of_birthdayV, state=VolunteerStates.date_of_birthday)
    dp.register_message_handler(get_educationV, state=VolunteerStates.education)
    dp.register_message_handler(get_professionV, state=VolunteerStates.profession)
    dp.register_message_handler(get_email, state=VolunteerStates.email)
        #dp.register_message_handler(check_photo_studV, lambda message: not message.photo, state=VolunteerStates.photo)
        #dp.register_message_handler(get_photoV, lambda message: message.photo, content_types=['photo'], state=VolunteerStates.photo)
    #Хочу в команду
    dp.register_message_handler(volunteer, Text(equals='Хочу в команду'))
    dp.register_message_handler(get_fio_team, state=ToTeamStates.fio)
    dp.register_message_handler(get_telephone_team, state=ToTeamStates.telephone)
    dp.register_message_handler(get_date_of_birthday_team, state=ToTeamStates.date_of_birthday)
    dp.register_message_handler(get_education_team, state=ToTeamStates.education)
    dp.register_message_handler(get_profession_team, state=ToTeamStates.profession)
    dp.register_message_handler(get_email_team, state=ToTeamStates.email)
        #dp.register_message_handler(check_photo_team, lambda message: not message.photo, state=ToTeamStates.photo)
        #dp.register_message_handler(get_photo_team, lambda message: message.photo, content_types=['photo'], state=ToTeamStates.photo)
    #Мероприятие
    dp.register_message_handler(event, Text(equals='Зарегистрироваться на мероприятии'))
    dp.register_message_handler(get_fio_event, state=EventStates.fio)
    dp.register_message_handler(get_telephone_event, state=EventStates.telephone)
    dp.register_message_handler(get_date_of_birthday_event, state=EventStates.date_of_birthday)
    dp.register_message_handler(get_education_event, state=EventStates.education)
    dp.register_message_handler(get_profession_event, state=EventStates.profession)
    dp.register_message_handler(get_email_event, state=EventStates.email)
    

