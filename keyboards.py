from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import database


async def inline_keyboard_chapters() -> InlineKeyboardMarkup:
    chapters_list = await database.get_topic_list()
    ikboard_chapters = InlineKeyboardMarkup(row_width=1)
    for topic in chapters_list:
        button = InlineKeyboardButton(text=f'{topic[1]}', callback_data=f'topics {topic[0]}')
        ikboard_chapters.add(button)
    return ikboard_chapters


async def ikeyboard_subtopic_admin(id_topic) -> InlineKeyboardMarkup:
    subchapters_list = await database.get_list_subtopics(id_topic)
    ikboard_subchapters = InlineKeyboardMarkup(row_width=2)
    if len(subchapters_list) >= 1:
        for subtopic in subchapters_list:
            button = InlineKeyboardButton(text=f'{subtopic[1]}', callback_data=f'subtopics {id_topic} {subtopic[0]}')
            ikboard_subchapters.add(button)
    ikboard_subchapters.add(InlineKeyboardButton(text='🖍 Редактировать', callback_data=f'change_topic {id_topic}'),
                            InlineKeyboardButton(text='🚯 Удалить', callback_data=f'delete_topic {id_topic}'))
    ikboard_subchapters.add(InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} 0'))
    ikboard_subchapters.add(InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close'))
    return ikboard_subchapters


async def ikeyboard_subtopic_user(id_topic) -> InlineKeyboardMarkup:
    subchapters_list = await database.get_list_subtopics(id_topic)
    ikboard_subchapters = InlineKeyboardMarkup(row_width=1)
    if len(subchapters_list) >= 1:
        for subtopic in subchapters_list:
            button = InlineKeyboardButton(text=f'{subtopic[1]}', callback_data=f'subtopics {id_topic} {subtopic[0]}')
            ikboard_subchapters.add(button)
    ikboard_subchapters.add(InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} 0'))
    ikboard_subchapters.add(InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close'))
    return ikboard_subchapters


async def inline_keyboard_user(id_topic, id_subtopic) -> InlineKeyboardMarkup:
    ikeyboard_user = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} {id_subtopic}')],
            [InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')]],
        row_width=1)
    return ikeyboard_user


async def inline_keyboard_admin(id_topic, id_subtopic) -> InlineKeyboardMarkup:
    ikeyboard_admin = InlineKeyboardMarkup()

    button1 = InlineKeyboardButton(text='🖍 Редактировать', callback_data=f'change_subtopic {id_topic} {id_subtopic}')
    button2 = InlineKeyboardButton(text='🚯 Удалить', callback_data=f'delete_subtopic {id_topic} {id_subtopic}')
    button3 = InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} {id_subtopic}')
    button4 = InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')
    ikeyboard_admin.add(button1, button2).add(button3).add(button4)
    return ikeyboard_admin


async def change_note(note_id) -> InlineKeyboardMarkup:
    ikeyboard_change = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text='🖍 Редактировать', callback_data=f'change_note {note_id}')
    button2 = InlineKeyboardButton(text='🚯 Удалить', callback_data=f'delete_note {note_id}')
    ikeyboard_change.add(button1, button2)
    return ikeyboard_change


ikeyboard_close_notes = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')]],
    row_width=1)

rkeyboard_user = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/cancel')],
                                               [KeyboardButton(text='/content')],
                                               [KeyboardButton(text='/change')],
                                               [KeyboardButton(text='/help')]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

rkeyboard_admin = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/cancel')],
                                                [KeyboardButton(text='/newtopic')],
                                                [KeyboardButton(text='/newsubtopic')],
                                                [KeyboardButton(text='/content')],
                                                [KeyboardButton(text='/change')],
                                                [KeyboardButton(text='/help')]],
                                      resize_keyboard=True,
                                      one_time_keyboard=True)