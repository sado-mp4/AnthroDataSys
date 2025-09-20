@dp.callback_query_handler(state=NewQuiz.walk)
async def add_class_out(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data != 'skip':
            data['walk'] = call.data
    await call.message.delete()
    #await call.message.answer('Напишите название товара', reply_markup=kb.cancel)
    #await call.message.answer('9️⃣ | Какова твоя четкость зрения?\n\nВведите число в формате X,YZ\nусреднённое для 2х глаз!\nНапример:\n• 2,00\n• 0,00\n• -1,75', reply_markup=kb.eye_contact_kb)
    #await NewQuiz.next()

#@dp.message_handler(content_types=types.ContentTypes.ANY, state=NewQuiz.eye_contact1)
#async def add_eye_contact_check(message: types.Message, state: FSMContext):
   # try:
       # number = float(message.text)
       # await NewQuiz.next()
    #except ValueError:
        #await message.answer("⚠️ | Введите число в формате X,YZ!\nНапример:\n• 2,00\n• 0,00\n• -1,75")
#  @dp.callback_query_handler(state=NewQuiz.eye_contact2)
#async def add_class_out(message: types.Message,call: types.CallbackQuery, state: FSMContext):
    #async with state.proxy() as data:
        #if call.data != 'skip':
            #data['eye_contact'] = float(message.text)
    await call.message.answer('9️⃣ | Имеется ли у тебя хобби, связанное со спортом?', reply_markup=kb.hobby_kb)
    await NewQuiz.next()
#@dp.message_handler(state=NewQuiz.hobby)
#async def add_hobby(call: types.CallbackQuery, state: FSMContext):
    #async with state.proxy() as data:
       # if call.data != 'skip':
            #data['hobby'] = call.data
    #await db.quiz_add_data(state)
    #await state.finish()
   # await call.message.delete()

@dp.message_handler(state=NewQuiz.hobby)
async def add_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
    await db.quiz_add_data(state)
    await message.answer('Товар успешно создан!', reply_markup=kb.main)
    await state.finish()

async def finish(message: types.Message):
        if message.from_user.id == int(os.getenv('ADMIN_ID1')) or int(os.getenv('ADMIN_ID2')):
            await message.answer(f'Данные успешно обработаны!',
                                 reply_markup=kb.main_admin)
        else:
            await message.answer(f'Данные успешно обработаны!',
                                 reply_markup=kb.main)