from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
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
        for topic in subchapters_list:
            button = InlineKeyboardButton(text=f'{topic[1]}', callback_data=f'subtopics {topic[0]}')
            ikboard_subchapters.add(button)
    ikboard_subchapters.add(InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close'))
    return ikboard_subchapters


ikeyboard_close = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='🔺 Закрыть 🔺', callback_data='close')]],
    row_width=1)
