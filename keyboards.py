from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
import database


async def inline_keyboard_chapters() -> InlineKeyboardMarkup:
    content_list = await database.get_topic_list()
    ikboard_chapters = InlineKeyboardMarkup(row_width=1)
    for topic in content_list:
        button = InlineKeyboardButton(text=f'{topic[1]}', callback_data=f'topics {topic[0]}')
        ikboard_chapters.add(button)
    return ikboard_chapters


inline_keyboard_close = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='⬆️ Закрыть ⬆️', callback_data='close')]],
    row_width=1)
