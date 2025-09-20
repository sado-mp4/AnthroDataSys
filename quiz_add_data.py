import sqlite3 as sq
from datetime import datetime

async def checkout(user_id):
    db = sq.connect('app/database/main.db')
    cur = db.cursor()
    prove = cur.execute("SELECT * FROM quiz_answers WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not prove:
        return False
    else:
        return True
async def quiz_add_data(state, user_id):
    db = sq.connect('app/database/main.db')
    cur = db.cursor()
    async with state.proxy() as data:
        cur.execute("""INSERT INTO quiz_answers (
                    tg_id,
                    unload,
                    time,
                    gender,
                    class_out,
                    hw_time,
                    general_ill,
                    bbone_ill,
                    neck_ill,
                    vascular_ill,
                    walk,
                    hobby) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (user_id,
                     data['unload'],
                     datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                     data['gender'],
                     data['class_out'],
                     data['hw_time'],
                     data['general_ill'],
                     data['bbone_ill'],
                     data['neck_ill'],
                     data['vascular_ill'],
                     data['walk'],
                     data['hobby']))
        db.commit()
        db.close()

async def del_str(user_id):
    db = sq.connect('app/database/main.db')
    cur = db.cursor()
    cur.execute("DELETE FROM quiz_answers WHERE tg_id == {key}".format(key=user_id)).fetchone()
    db.commit()
    db.close()