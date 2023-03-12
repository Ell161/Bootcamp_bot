from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import database


async def inline_keyboard_chapters() -> InlineKeyboardMarkup:
    chapters_list = await database.get_topic_list()
    ikboard_chapters = InlineKeyboardMarkup(row_width=1)
    for topic in chapters_list:
        button = InlineKeyboardButton(text=f'{topic[1]}', callback_data=f'topics {topic[0]}')
        ikboard_chapters.add(button)
    return ikboard_chapters


async def inline_keyboard_subchapters(id_topic) -> InlineKeyboardMarkup:
    subchapters_list = await database.get_list_subtopics(id_topic)
    ikboard_subchapters = InlineKeyboardMarkup(row_width=1)
    if len(subchapters_list) >= 1:
        for subtopic in subchapters_list:
            button = InlineKeyboardButton(text=f'{subtopic[1]}', callback_data=f'subtopics {id_topic} {subtopic[0]}')
            ikboard_subchapters.add(button)
    ikboard_subchapters.add(InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} 0'))
    ikboard_subchapters.add(InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close'))
    return ikboard_subchapters


async def inline_keyboard_close(id_topic, id_subtopic) -> InlineKeyboardMarkup:
    ikeyboard_close = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='🖍 Добавить заметку', callback_data=f'note {id_topic} {id_subtopic}')],
                         [InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')]],
        row_width=1)
    return ikeyboard_close


async def change_note(note_id) -> InlineKeyboardMarkup:
    ikeyboard_change = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='🖍 Редактировать', callback_data=f'change_note {note_id}')],
                         [InlineKeyboardButton(text='🚯 Удалить', callback_data=f'delete_note {note_id}')]],
        row_width=1)
    return ikeyboard_change


ikeyboard_close_notes = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')]],
        row_width=1)
