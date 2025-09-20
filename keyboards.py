from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
#Основная клавиатура пользователя
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('✍ Заполнить анкету').add('📊 Составить отчет').add('⚙️ Настройки')

include = ReplyKeyboardMarkup(resize_keyboard=True)
include.add('🗑 Удалить анкету')

#Основная клавиатура админа
include_admin = ReplyKeyboardMarkup(resize_keyboard=True)
include_admin.add('🗑 Удалить анкету')

prove1by1 = ReplyKeyboardMarkup(resize_keyboard=True)
prove1by1.add('✍ Перезаписать ответ').add('В главное меню')

#Система администрирования (не работает)
sys_main = ReplyKeyboardMarkup(resize_keyboard=True)
sys_main.add('Пусто')

#Тестовая клавиатура
test_id= InlineKeyboardMarkup(row_width=2)
test_id.add(InlineKeyboardButton(text='Заполнить анкету', url ='https://vk.com/feed'),
            InlineKeyboardButton(text='Об инструменте', url ='https://vk.com/feed'),
            InlineKeyboardButton(text='О авторах', url ='https://vk.com/feed'),
            InlineKeyboardButton(text='Test1', url ='https://vk.com/feed'),
            InlineKeyboardButton(text='Test2', url ='https://vk.com/feed'))

#Тестирование с инлайн-кнопками
gender_kb= InlineKeyboardMarkup(row_width=2)
gender_kb.add(InlineKeyboardButton(text='Мужской', callback_data='men'),
            InlineKeyboardButton(text='Женский', callback_data='women'))

class_out_kb= InlineKeyboardMarkup(row_width=3)
class_out_kb.add(InlineKeyboardButton(text='7-ой', callback_data='7'),
            InlineKeyboardButton(text='8-ой', callback_data= '8'),
            InlineKeyboardButton(text='9-ой', callback_data='9'),
            InlineKeyboardButton(text='10-й', callback_data='10'),
            InlineKeyboardButton(text='11-й', callback_data='11'))

hw_time_kb= InlineKeyboardMarkup(row_width=2)
hw_time_kb.add(InlineKeyboardButton(text='от 0,5 - 1 часа', callback_data='over0.5to1'),
            InlineKeyboardButton(text='от 1 - 2 часов', callback_data='over1to2'),
            InlineKeyboardButton(text='от 2 - 4 часов', callback_data='over2to4'),
            InlineKeyboardButton(text='свыше 4 часов', callback_data='over4'),
            InlineKeyboardButton(text='У меня нет свободного времени', callback_data='notenough'))


general_ill_time_kb= InlineKeyboardMarkup(row_width=1)
general_ill_time_kb.add(InlineKeyboardButton(text='Реже 1 раза/пол года', callback_data='past1bbill'),
            InlineKeyboardButton(text='1 раз/пол года', callback_data='1bbill'),
            InlineKeyboardButton(text='1 раз/3 мес', callback_data='1p3bbill'),
            InlineKeyboardButton(text='1 раз/мес', callback_data='1p1bbill'),
            InlineKeyboardButton(text='Чаще 1 раз/мес', callback_data='over1p1bbill'))

bbone_ill_kb= InlineKeyboardMarkup(row_width=1)
bbone_ill_kb.add(InlineKeyboardButton(text='У меня нет искревлений позвоночника', callback_data='bbonenone'),
            InlineKeyboardButton(text='1 степень', callback_data='bbone1'),
            InlineKeyboardButton(text='2 степень', callback_data='bbone2'),
            InlineKeyboardButton(text='3 степень', callback_data='bbone3'),
            InlineKeyboardButton(text='4 степень', callback_data='bbone4'))

neck_ill_kb= InlineKeyboardMarkup(row_width=1)
neck_ill_kb.add(InlineKeyboardButton(text='Болит часто, лечу по рекомендациям врача', callback_data='neck1'),
            InlineKeyboardButton(text='Болит редко, лечу без рекомендаций врача',
                                 callback_data='neck2'),
            InlineKeyboardButton(text='Практически не болит (очень редко)', callback_data='neck3'),
            InlineKeyboardButton(text='Никогда не сталкивался(ась) с этим', callback_data='neck4'),
            InlineKeyboardButton(text='Пропустить', callback_data='skip'))

vascular_ill_kb= InlineKeyboardMarkup(row_width=2)
vascular_ill_kb.add(InlineKeyboardButton(text='Да', callback_data='Y'),
            InlineKeyboardButton(text='Нет',
                                 callback_data='N'),
            InlineKeyboardButton(text='Пропустить', callback_data='skip'))

walk_kb= InlineKeyboardMarkup(row_width=1)
walk_kb.add(InlineKeyboardButton(text='Каждый день', callback_data='walk1'),
            InlineKeyboardButton(text='1 раз/2 дня',
                                 callback_data='walk2'),
            InlineKeyboardButton(text='2 раз/нед',
                                 callback_data='walk3'),
            InlineKeyboardButton(text='1 раз/нед',
                                 callback_data='walk4'),
            InlineKeyboardButton(text='Реже 1 раз/нед',
                                 callback_data='walk5'),
            InlineKeyboardButton(text='Пропустить', callback_data='skip'))

eye_contact_kb= InlineKeyboardMarkup(row_width=1)
eye_contact_kb.add(InlineKeyboardButton(text='Пропустить', callback_data='skip'))

hobby_kb= InlineKeyboardMarkup(row_width=2)
hobby_kb.add(InlineKeyboardButton(text='Да', callback_data='Y'),
            InlineKeyboardButton(text='Нет',
                                 callback_data='N'),
            InlineKeyboardButton(text='Пропустить', callback_data='skip'))






