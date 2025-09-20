#Загрузка необходимых компонентов
print('Импорт компонентов')
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from app import keyboards as kb
from app.database import database_callcenter as db
from app.database import quiz_add_data as qad
from app.database import report_creator as rc
from dotenv import load_dotenv
import os
print('Бот запускается...')

#Инициализация переменных
storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv('SSSH'))
dp = Dispatcher(bot=bot, storage=storage)

class NewQuiz(StatesGroup):
    gender = State()
    class_out = State()
    hw_time = State()
    general_ill = State()
    bbone_ill = State()
    neck_ill = State()
    vascular_ill = State()
    walk = State()
    hobby = State()
    plus = State()



#Запуск базы данных
async def on_startup(_):
    await db.db_start()

#Инициализация клавиатур из файла keyboards.py
#Метод авторизации
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    global tg_id
    tg_id = message.from_user.id
    await db.cmd_start_db(tg_id)
    await message.delete()
    if tg_id == int(os.getenv('ADMIN_ID1')) or int(os.getenv('ADMIN_ID2')):
        #await message.answer_sticker('CAACAgIAAxkBAAM_ZlnKV1TRjfXnZL7aLqYa1rYtvlYAAh4JAAIYQu4I-VjZ7h0hnCE1BA')
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!\n\nДля начала работы заполни форму, по кнопке \n✍ Заполнить анкету\nСледущим шагом, можно получить рекомендации по дальнейшему состоянию здоровья \n📊 Составить отчет',
                             reply_markup=kb.main)
    else:
        #await message.answer_sticker('CAACAgIAAxkBAAM9ZlnKScRhbG9VrNGrjKG1Qs01sS0AAjgLAAJO5JlLMrFH0tlPjNA1BA')
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!\n\nДля начала работы заполни форму, по кнопке \n✍ Заполнить анкету\nСледущим шагом, можно получить рекомендации по дальнейшему состоянию здоровья \n📊 Составить отчет',
                         reply_markup=kb.main)

@dp.message_handler(text='⚙️ Настройки')
async def cmd_start(message: types.Message):
    global tg_id
    tg_id = message.from_user.id
    await db.cmd_start_db(tg_id)
    await message.delete()
    if tg_id == 947879887 or int(os.getenv('ADMIN_ID2')):
        await message.answer(f'Настройки',
                             reply_markup=kb.include_admin)
    else:
        await message.answer(f'Настройки',
                         reply_markup=kb.include)
#Заполнение анкеты
@dp.message_handler(text='✍ Заполнить анкету')
async def add_answer(message: types.Message, state: FSMContext):
    if await qad.checkout(message.from_user.id) == False:
        await bot.forward_message(os.getenv('CHAT_CONFIG'), message.from_user.id, message.message_id)
        await NewQuiz.gender.set()
        await message.delete()
        async with state.proxy() as data:
            data['unload'] = None
        await message.answer('1️⃣ | Твой пол', reply_markup=kb.gender_kb)
    else:
        await message.answer('⚠️ | Ты уже заполнял анкенту. Перезаписать твой ответ?', reply_markup=kb.prove1by1)

@dp.message_handler(text='✍ Перезаписать ответ')
async def add_answer(message: types.Message, state: FSMContext):
        await bot.forward_message(os.getenv('CHAT_CONFIG'), message.from_user.id, message.message_id)
        await qad.del_str(message.from_user.id)
        await NewQuiz.gender.set()
        async with state.proxy() as data:
            data['unload'] = None
            data['unload'] = "Y"
        await message.answer('1️⃣ | Твой пол', reply_markup=kb.gender_kb)

@dp.message_handler(text='🗑 Удалить анкету')
async def add_answer(message: types.Message, state: FSMContext):
        await bot.forward_message(os.getenv('CHAT_CONFIG'), message.from_user.id, message.message_id)
        await qad.del_str(message.from_user.id)
        await message.answer(f'Данные очищены!',
                             reply_markup=kb.main)

@dp.message_handler(text='В главное меню')
async def cmd_start(message: types.Message):
    await message.delete()
    if tg_id == int(os.getenv('ADMIN_ID1')) or int(os.getenv('ADMIN_ID2')):
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!\n\nДля начала работы заполни форму, по кнопке \n✍ Заполнить анкету\nСледущим шагом, можно получить рекомендации по дальнейшему состоянию здоровья \n📊 Составить отчет',
                             reply_markup=kb.main)
    else:
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!\n\nДля начала работы заполни форму, по кнопке \n✍ Заполнить анкету\nСледущим шагом, можно получить рекомендации по дальнейшему состоянию здоровья \n📊 Составить отчет',
                         reply_markup=kb.main)

@dp.callback_query_handler(state=NewQuiz.gender)
async def add_gender(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = call.data
    await call.message.delete()
    await call.message.answer('2️⃣ | Какой класс ты окончил(а)?\n(2023-2024г)', reply_markup=kb.class_out_kb)
    await state.set_state(NewQuiz.class_out.state)

@dp.callback_query_handler(state=NewQuiz.class_out)
async def add_class_out(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['class_out'] = call.data
    await call.message.delete()
    await call.message.answer('3️⃣ | Какое кол-во времени, проводимое за выполнением дз/просмотром лекций у тебя занимает в день?\n(выше школьного уровня)', reply_markup=kb.hw_time_kb)
    await state.set_state(NewQuiz.hw_time.state)

@dp.callback_query_handler(state=NewQuiz.hw_time)
async def add_hw_time(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['hw_time'] = call.data
        data['general_ill'] = None
    await call.message.delete()
    await call.message.answer('4️⃣ | Какова твоя частота заболеваемости?\n(Сезонные простудные заболевания, обострение хронических заболеваний и др)', reply_markup=kb.general_ill_time_kb)
    await state.set_state(NewQuiz.general_ill.state)

@dp.callback_query_handler(state=NewQuiz.general_ill)
async def add_general_ill(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['general_ill'] = call.data
        data['bbone_ill'] = None
    await call.message.delete()
    await call.message.answer('5️⃣ | Имеется ли наличие искривления позвоночника?\n(Если да, то степень искривления, если ты обследовался(ась) у врача)', reply_markup=kb.bbone_ill_kb)
    await state.set_state(NewQuiz.bbone_ill.state)

@dp.callback_query_handler(state=NewQuiz.bbone_ill)
async def add_bbone_ill(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['bbone_ill'] = call.data
        data['neck_ill'] = None
    await call.message.delete()
    await call.message.answer('6️⃣ | Имеется ли наличие проблем с шейным отделом?\n(Если да, как часто шея болит/ощущается дискомфорт)', reply_markup=kb.neck_ill_kb)
    await state.set_state(NewQuiz.neck_ill.state)

@dp.callback_query_handler(state=NewQuiz.neck_ill)
async def add_neck_ill(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data != 'skip':
            data['neck_ill'] = call.data
        data['vascular_ill'] = None
    await call.message.delete()
    await call.message.answer('7️⃣ | Имеется ли наличие вегето-сосудистых заболеваний?', reply_markup=kb.vascular_ill_kb)
    await state.set_state(NewQuiz.vascular_ill.state)

@dp.callback_query_handler(state=NewQuiz.vascular_ill)
async def add_vascular_ill(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data != 'skip':
            data['vascular_ill'] = call.data
        data['walk'] = None
    await call.message.delete()
    await call.message.answer('8️⃣ | Как часто ты гуляешь?', reply_markup=kb.walk_kb)
    await state.set_state(NewQuiz.walk.state)

@dp.callback_query_handler(state=NewQuiz.walk)
async def add_walk(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data != 'skip':
            data['walk'] = call.data
        data['hobby'] = None
    await call.message.delete()
    await call.message.answer('9️⃣ | Имеется ли у тебя хобби, связанное со спортом?', reply_markup=kb.hobby_kb)
    await state.set_state(NewQuiz.hobby.state)

@dp.callback_query_handler(state=NewQuiz.hobby)
async def add_hobby(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data != 'skip':
            data['hobby'] = call.data
    await qad.quiz_add_data(state, tg_id)
    await state.finish()
    await call.message.delete()
    if call.message.from_user.id == int(os.getenv('ADMIN_ID1')) or int(os.getenv('ADMIN_ID2')):
            await call.message.answer(f'Данные успешно обработаны!',
                                 reply_markup=kb.main)
    else:
            await call.message.answer(f'Данные успешно обработаны!',
                                 reply_markup=kb.main)
@dp.message_handler(text='📊 Составить отчет')
async def report(message: types.Message):
    so_extract = await rc.report_call(message.from_user.id)
    class_out_begin = await rc.report_callin(so_extract)
    await message.answer(f'{message.from_user.first_name}, для тебя по полученным данным был составлен отчет.\n\nПредпологаемый класс: {class_out_begin}\n'
                         f'Спрогнозированное состояние здоровья значится искривлением позвоночника 1 степени и проблемами с шейным отделом (чаще из-за долгой неподвижности). Рекомендуется почаще организовывать прогулки на улице и заниматься спортом.')
@dp.message_handler(text='⚙️ Система администрирования')
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID1')) or int(os.getenv('ADMIN_ID2')):
        await bot.forward_message(os.getenv('CHAT_CONFIG'), message.from_user.id, message.message_id)
        await message.answer(f'panel has open',
                             reply_markup=kb.sys_main)
    else:
        await message.reply('Оу! Я тебя не понимаю, воспользуйся клавиатурой для навигации.')
@dp.message_handler()
async def answer(message: types.Message):
   await message.reply('Оу! Я тебя не понимаю, воспользуйся клавиатурой для навигации. Тестовая версия, воспользуйтесь /start')

#Начало работы
if __name__ == '__main__':
    print('Бот запущен! https://t.me/AnthroDataBot')
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

