import sqlite3 as sq
from datetime import datetime
async def db_start():
        global db, cur
        db = sq.connect('app/database/main.db')
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "tg_id INTEGER, "
                    "cart_id TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS quiz_answers("
                    "q_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "tg_id INTEGER, "
                    "unload TEXT DEFAULT N,"
                    "time TEXT,"
                    "gender TEXT,"
                    "class_out NUMERIC, "
                    "hw_time TEXT, "
                    "general_ill TEXT, "
                    "bbone_ill TEXT, "
                    "neck_ill TEXT, "
                    "vascular_ill TEXT, "
                    "walk TEXT, "
                    "hobby TEXT )")
        db.commit()
        db.close()
async def cmd_start_db(user_id):
    db = sq.connect('app/database/main.db')
    cur = db.cursor()
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()
        db.close()

