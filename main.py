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


@dp.callback_query_handler()
async def content_desc(callback: types.CallbackQuery):
    cb_date = callback.data.split()
    if cb_date[0] == 'close':
        await callback.message.delete()
    elif cb_date[0] == 'topics':
        topic = await database.get_topic_description(cb_date[1])
        ikboard_subchapters = await keyboards.inline_keyboard_subchapters(id_topic=cb_date[1])
        await bot.send_photo(chat_id=callback.message.chat.id, photo=topic[0],
                             caption=f'<b>{topic[2]}</b>\n\n<i>{topic[3]}</i>',
                             reply_markup=ikboard_subchapters)


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
