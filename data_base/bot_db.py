import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена')

    db.execute("CREATE TABLE IF NOT EXISTS menu"
               "(photo TEXT, name TEXT, info TEXT,"
               " price INTEGER)")
    db.commit()



