import sqlite3 as sq
db = sq.connect('app/database/main.db')
cur = db.cursor()

    #Анализируем строчку пользователя
data_all = cur.execute("SELECT * FROM quiz_answers WHERE tg_id == {key}".format(key=947879888)).fetchone()

original_row = {
        'q_id': data_all[0],
        'tg_id': data_all[1],
        'unload': data_all[2],
        'time': data_all[3],
        'gender': data_all[4],
        'class_out': data_all[5],
        'hw_time': data_all[6],
        'general_ill': data_all[7],
        'bbone_ill': data_all[8],
        'neck_ill': data_all[9],
        'vascular_ill': data_all[10],
        'walk': data_all[11],
        'hobby': data_all[12]}

def count_matching_values(row1, row2):
        matches = sum(1 for key in row1 if row1[key] == row2.get(key))
        return matches
# Проверка на класс
if data_all[5] == 7: cur.execute("SELECT * FROM quiz_answers WHERE class_out <= 10 AND NOT class_out = 8")
if data_all[5] == 8: cur.execute("SELECT * FROM quiz_answers WHERE class_out >= 9")
if data_all[5] == 9: cur.execute("SELECT * FROM quiz_answers WHERE class_out >= 10")
if data_all[5] == 10: cur.execute("SELECT * FROM quiz_answers class_out >= 11")


    # Получение всех строк из таблицы
all_rows = cur.fetchall()

    # Создание списка для хранения количества совпадений для каждой строки
matching_counts = []

    # Сравнение каждой строки с исходной и подсчёт совпадений
for row in all_rows:
        row_dict = {
            'q_id': row[0],
            'tg_id': row[1],
            'unload': row[2],
            'time': row[3],
            'gender': row[4],
            'class_out': row[5],
            'hw_time': row[6],
            'general_ill': row[7],
            'bbone_ill': row[8],
            'neck_ill': row[9],
            'vascular_ill': row[10],
            'walk': row[11],
            'hobby': row[12]}
        matching_counts.append((row, count_matching_values(original_row, row_dict)))
    # Сортировка списка по количеству совпадений в убывающем порядке
matching_counts.sort(key=lambda x: x[1], reverse=True)

so_extract = []
    # Вывод 5 самых совпадающих строк, исключая первую - нашу!
for row, matches in matching_counts[:5]:
    so_extract.append(row)

so_extract_1 = so_extract[0]
so_extract_2 = so_extract[1]
so_extract_3 = so_extract[2]
so_extract_4 = so_extract[3]
so_extract_5 = so_extract[4]
print(so_extract)

