import sqlite3
from typing import List, Any


async def db_connect() -> None:
    """Connecting to a database, creating database tables."""

    global base, cursor

    base = sqlite3.connect('bootcamp_db.db')
    cursor = base.cursor()
    base.execute("""CREATE TABLE IF NOT EXISTS topics(
                                ID_topic INTEGER PRIMARY KEY AUTOINCREMENT,
                                photo_id TEXT,
                                title TEXT,
                                head TEXT,
                                description TEXT)""")
    base.execute("""CREATE TABLE IF NOT EXISTS subtopics(
                                    ID_subtopic INTEGER PRIMARY KEY AUTOINCREMENT,
                                    topic INTEGER,
                                    title TEXT,
                                    head TEXT,
                                    description TEXT)""")
    base.execute("""CREATE TABLE IF NOT EXISTS notes(
                                        ID_note INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id TEXT,
                                        topic INTEGER,
                                        subtopic INTEGER DEFAULT 0,
                                        head TEXT,
                                        description TEXT)""")
    base.commit()


async def save_topic_db(state) -> None:
    """The function saves the topic data to the database"""

    async with state.proxy() as data:
        cursor.execute('INSERT INTO topics (photo_id, title, head, description) VALUES(?, ?, ?, ?)',
                       (data['photo'], data['title'], data['head'], data['description']))
        base.commit()


async def get_topic_list() -> List[tuple]:
    """The function displays a list of topic with information about the topic id and name"""

    cursor.execute('SELECT ID_topic, title FROM topics ORDER BY ID_topic')
    value = cursor.fetchall()
    base.commit()
    return value


async def get_topic_description(id_topic) -> list:
    """The function displays a description of topic"""

    cursor.execute(f'SELECT photo_id, title, head, description FROM topics WHERE ID_topic = "{id_topic}"')
    value = cursor.fetchall()
    base.commit()
    return value[0]


async def save_subtopic_db(state) -> None:
    """The function saves the subtopic data to the database"""

    async with state.proxy() as data:
        cursor.execute('INSERT INTO subtopics (topic, title, head, description) VALUES(?, ?, ?, ?)',
                       (data['title'], data['subtitle'], data['head'], data['description']))
        base.commit()


async def get_list_subtopics(id_topic) -> List[tuple]:
    """The function displays a list of subtopic with information about the subtopic id and name"""

    cursor.execute(f'SELECT ID_subtopic, title FROM subtopics WHERE topic = {id_topic}')
    value = cursor.fetchall()
    base.commit()
    return value


async def get_subtopic_description(id_subtopic) -> List[tuple]:
    """The function displays a description of subtopic"""

    cursor.execute(f'SELECT head, description FROM subtopics WHERE ID_subtopic = "{id_subtopic}"')
    value = cursor.fetchall()
    base.commit()
    return value[0]


async def save_note_db(state) -> None:
    """The function saves the note data to the database"""

    async with state.proxy() as data:
        cursor.execute('INSERT INTO notes (user_id, topic, subtopic, head, description) VALUES(?, ?, ?, ?, ?)',
                       (data['user_id'], data['topic'], data['subtopic'], data['head'], data['description']))
        base.commit()


async def get_all_notes(user_id) -> List[tuple]:
    """The function displays all notes with description"""

    cursor.execute(f'SELECT ID_note, head, description FROM notes WHERE user_id = "{user_id}"')
    value = cursor.fetchall()
    base.commit()
    return value


async def delete_note(note_id) -> None:
    """The function deletes the note from the database"""

    cursor.execute(f'DELETE FROM notes WHERE ID_note = "{note_id}"')
    base.commit()


async def update_note_db(state) -> None:
    """The function updates the note information from the database"""

    async with state.proxy() as data:
        cursor.execute('UPDATE notes SET head = "{head}", description = "{description}" '
                       'WHERE ID_note = "{note_id}"'.format(head=data['head'],
                                                            description=data['description'],
                                                            note_id=data['note_id']))
    base.commit()


async def update_topic_db(state) -> None:
    """The function updates the topic information from the database"""

    async with state.proxy() as data:
        cursor.execute('''UPDATE topics SET 
        photo_id = "{photo_id}", 
        title = "{title}", 
        head = "{head}", 
        description = "{description}"
        WHERE ID_topic = "{topic_id}"'''.format(photo_id=data['photo'],
                                                title=data['title'],
                                                head=data['head'],
                                                description=data['description'],
                                                topic_id=data['topic_id']))
    base.commit()


async def update_subtopic_db(state) -> None:
    """The function updates the subtopic information from the database"""

    async with state.proxy() as data:
        cursor.execute('''UPDATE subtopics SET  
        head = "{head}", 
        description = '{description}' 
        WHERE ID_subtopic = "{subtopic_id}"'''.format(head=data['head'],
                                                      description=data['description'],
                                                      subtopic_id=data['subtopic_id']))
    base.commit()


async def delete_subtopic(subtopic_id) -> None:
    """The function deletes the subtopic from the database"""

    cursor.execute(f'DELETE FROM subtopics WHERE ID_subtopic = "{subtopic_id}"')
    base.commit()


async def delete_topic(topic_id) -> None:
    """The function deletes the subtopic from the database"""

    cursor.execute(f'DELETE FROM subtopics WHERE topic = "{topic_id}"')
    cursor.execute(f'DELETE FROM topics WHERE ID_topic = "{topic_id}"')
    base.commit()
