from typing import Dict, Any

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import database
import variables
import keyboards
from Bootcamp_bot.config import TOKEN_API, admin_id

storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


class FSMTopics(StatesGroup):
    """FSM class of states for bootcamp chapters"""

    photo = State()
    title = State()
    head = State()
    description = State()


class FSMSubTopics(StatesGroup):
    """FSM class of states for subchapters"""

    title = State()
    subtitle = State()
    head = State()
    description = State()


class FSMNotes(StatesGroup):
    """FSM class of states for notes"""

    head = State()
    description = State()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message) -> None:
    """The function greets the user and displays a list of bootcamp chapters"""

    keyboard_content = await keyboards.inline_keyboard_chapters()
    await bot.send_message(chat_id=message.from_user.id, text=variables.start_command_text,
                           reply_markup=keyboard_content)
    await message.delete()


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message) -> None:
    """TThe function outputs a list of commands"""

    if message.from_user.id == admin_id:
        await bot.send_message(chat_id=message.from_user.id, text=variables.help_command_admin)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=variables.help_command_user)
    await message.delete()


@dp.message_handler(commands=['content'])
async def command_content(message: types.Message) -> None:
    """TThe function outputs a list of chapters"""

    keyboard_content = await keyboards.inline_keyboard_chapters()
    await bot.send_message(chat_id=message.from_user.id, text=variables.content, reply_markup=keyboard_content)
    await message.delete()


@dp.message_handler(commands=['change'])
async def command_content(message: types.Message) -> None:
    """TThe function delete a note"""

    await message.delete()
    note_list = await database.get_all_notes(user_id=message.from_user.id)
    if len(note_list) >= 1:
        for note in note_list:
            ikeyboard_delete = await keyboards.change_note(note_id=note[0])
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f'<b>{note[1]}</b>\n\n<i>{note[2]}</i>',
                                   reply_markup=ikeyboard_delete)


@dp.message_handler(commands=['cancel'], state='*')
async def cansel_create(message: types.Message, state: FSMContext):
    """The function cancels the creation of a chapter or a subchapter"""

    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


@dp.message_handler(lambda message: message.from_user.id == admin_id, commands=['newtopic'], state=None)
async def create_topic(message: types.Message) -> None:
    """The function processes the administrator's request to create a new chapter"""

    await message.delete()
    await FSMTopics.photo.set()
    await message.answer(text=variables.get_photo)


@dp.message_handler(lambda message: not message.photo, state=FSMTopics.photo)
async def check_photo(message: types.Message) -> None:
    """The function makes the verification of sending a photo by the administrator"""

    await message.reply(text=variables.not_photo)


@dp.message_handler(content_types=['photo'], state=FSMTopics.photo)
async def get_photo_topic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the administrator's photo and transfers it to the next FSM waiting state."""

    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMTopics.next()
    await message.answer(text=variables.get_title)


@dp.message_handler(state=FSMTopics.title)
async def get_title_topic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the chapter title and transfers it to the next FSM waiting state."""

    if len(message.text) > 50:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['title'] = message.text
        await FSMTopics.next()
        await message.answer(text=variables.get_head)


@dp.message_handler(state=FSMTopics.head)
async def get_head_topic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the chapter head and transfers it to the next FSM waiting state."""

    if len(message.text) > 50:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['head'] = message.text
        await FSMTopics.next()
        await message.answer(text=variables.get_desc)


@dp.message_handler(state=FSMTopics.description)
async def get_description_topic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the chapter description and  saves data to the database,
    closes the state machine."""

    if len(message.text) > 970:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['description'] = message.text
        await database.save_topic_db(state)
        await message.answer(text=variables.final_create)
        await state.finish()


@dp.message_handler(lambda message: message.from_user.id == admin_id, commands=['newsubtopic'], state=None)
async def create_subtopic(message: types.Message) -> None:
    """The function processes the administrator's request to create a new subchapter"""

    await message.delete()
    await FSMSubTopics.title.set()
    keyboard_select_topic = await keyboards.inline_keyboard_chapters()
    await message.answer(text=variables.select_topic, reply_markup=keyboard_select_topic)


@dp.callback_query_handler(state=FSMSubTopics.title)
async def get_subtopic_title(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """The function makes the subtitle by the administrator and transfers it to the next FSM waiting state"""

    async with state.proxy() as data:
        title = callback_query.data.split()
        data["title"] = title[1]
    await FSMSubTopics.next()
    await callback_query.message.answer(text=variables.get_subtitle)


@dp.message_handler(state=FSMSubTopics.subtitle)
async def get_subtitle(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the subchapter title and transfers it to the next FSM waiting state."""

    if len(message.text) > 50:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['subtitle'] = message.text
        await FSMSubTopics.next()
        await message.answer(text=variables.get_head)


@dp.message_handler(state=FSMSubTopics.head)
async def get_head_subtopic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the subchapter head and transfers it to the next FSM waiting state."""

    if len(message.text) > 255:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['head'] = message.text
        await FSMSubTopics.next()
        await message.answer(text=variables.get_desc)


@dp.message_handler(state=FSMSubTopics.description)
async def get_description_subtopic(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the subchapter description and  saves data to the database,
    closes the state machine."""

    async with state.proxy() as data:
        data['description'] = message.text
    await database.save_subtopic_db(state)
    await message.answer(text=variables.final_create)
    await state.finish()


@dp.message_handler(state=FSMNotes.head)
async def get_head_note(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the subchapter head and transfers it to the next FSM waiting state."""

    if len(message.text) > 255:
        await message.reply(text=variables.too_long)
    else:
        async with state.proxy() as data:
            data['head'] = message.text
        await FSMNotes.next()
        await message.answer(text=variables.get_desc)


@dp.message_handler(state=FSMNotes.description)
async def get_description_note(message: types.Message, state: FSMContext) -> None:
    """The function receives data about the subchapter description and  saves data to the database,
    closes the state machine."""

    async with state.proxy() as data:
        data['description'] = message.text
    try:
        await state.get_data(data['note_id'])
        await database.update_note_db(state)
    except KeyError:
        await database.save_note_db(state)
    await message.answer(text=variables.final_create)
    await state.finish()


@dp.callback_query_handler()
async def content_desc(callback: types.CallbackQuery, state: FSMContext):
    callback_info = callback.data.split()
    action = callback_info[0]

    match action:
        case 'close':
            await callback.message.delete()

        case 'topics':
            topic = await database.get_topic_description(callback_info[1])
            ikboard_subchapters = await keyboards.inline_keyboard_subchapters(id_topic=callback_info[1])
            await bot.send_photo(chat_id=callback.message.chat.id, photo=topic[0],
                                 caption=f'<b>{topic[2]}</b>\n\n<i>{topic[3]}</i>',
                                 reply_markup=ikboard_subchapters)
            user_notes = await database.get_user_notes_for_topic(user_id=callback.from_user.id,
                                                                 topic_id=callback_info[1])
            if user_notes is not None:
                await bot.send_message(chat_id=callback.message.chat.id, text=user_notes,
                                       reply_markup=keyboards.ikeyboard_close_notes)

        case 'subtopics':
            subtopic = await database.get_subtopic_description(callback_info[2])
            ikeyboard_close = await keyboards.inline_keyboard_close(id_topic=callback_info[1],
                                                                    id_subtopic=callback_info[2])
            await bot.send_message(chat_id=callback.message.chat.id,
                                   text=f'<b>{subtopic[0]}</b>\n\n<i>{subtopic[1]}</i>',
                                   reply_markup=ikeyboard_close)
            user_notes = await database.get_user_notes_for_subtopic(user_id=callback.from_user.id,
                                                                    topic_id=callback_info[1],
                                                                    subtopic_id=callback_info[2])
            if user_notes is not None:
                await bot.send_message(chat_id=callback.message.chat.id, text=user_notes,
                                       reply_markup=keyboards.ikeyboard_close_notes)

        case 'note':
            await FSMNotes.head.set()
            async with state.proxy() as data:
                data['user_id'] = callback.from_user.id
                data['topic'] = callback_info[1]
                data['subtopic'] = callback_info[2]
            await callback.message.answer(text=variables.get_head)

        case 'delete_note':
            await database.delete_note(note_id=callback_info[1])
            await callback.answer(text=variables.delete_info)
            await callback.message.delete()

        case 'change_note':
            await FSMNotes.head.set()
            async with state.proxy() as data:
                data['note_id'] = callback_info[1]
            await callback.message.answer(text=variables.get_head)


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer(text=variables.empty)
    await message.delete()


async def on_startup(_):
    await database.db_connect()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
