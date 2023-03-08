import sqlite3
from typing import List, Any


async def db_connect() -> None:
    global base, cursor

    base = sqlite3.connect('bootcamp_db.db')
    cursor = base.cursor()
    base.execute("""CREATE TABLE IF NOT EXISTS topics(
                                ID_topic INTEGER PRIMARY KEY AUTOINCREMENT,
                                photo_id TEXT,
                                title TEXT,
                                description TEXT)""")
    base.commit()


async def save_topic_db(state) -> None:
    async with state.proxy() as data:
        cursor.execute('INSERT INTO topics (photo_id, title, description) VALUES(?, ?, ?)',
                       (data['photo'], data['title'], data['description']))
        base.commit()


async def get_topic_list() -> List[tuple]:
    cursor.execute('SELECT ID_topic, title FROM topics ORDER BY ID_topic')
    value: List[tuple] = cursor.fetchall()
    base.commit()
    return value


#async def get_topic_description():
#    cursor.execute('SELECT description FROM topics WHERE ')
#    value = cursor.fetchall()
#    base.commit()
#    return value
