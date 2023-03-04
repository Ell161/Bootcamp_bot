from aiogram import Bot, Dispatcher, executor, types
import keyboards
import variables
from Bootcamp_bot.config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=variables.help_command_text,
                           parse_mode="HTML")


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=variables.start_command_text,
                           parse_mode="HTML",
                           reply_markup=keyboards.inline_keyboard_modules)
    await message.delete()


@dp.callback_query_handler(text='close')
async def close_keyboard(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler()
async def start_callback(callback: types.CallbackQuery):
    if callback.data == 'Algorithms':
        photo = open('img/algorithm.jpg', 'rb')
        return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                             photo=photo, caption=variables.Algorithms, parse_mode='HTML',
                                             reply_markup=keyboards.inline_keyboard_algorithms)
    elif callback.data == 'TCP/IP':
        photo = open('img/server.jpg', 'rb')
        return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                             photo=photo, caption=variables.TCP_IP, parse_mode='HTML',
                                             reply_markup=keyboards.inline_keyboard_TCP)
    elif callback.data == 'Python':
        photo = open('img/python.jpg', 'rb')
        return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                             photo=photo, caption=variables.Python, parse_mode='HTML',
                                             reply_markup=keyboards.inline_keyboard_python)
    elif callback.data == 'Multithreading':
        photo = open('img/multithreading.jpg', 'rb')
        return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                             photo=photo, caption=variables.Multithreading, parse_mode='HTML',
                                             reply_markup=keyboards.inline_keyboard_multithreading)


@dp.callback_query_handler()
async def algorithm_callback(callback: types.CallbackQuery):
    if callback.data == 'algorithm complexity':
        return await callback.answer(text='algorithm complexity')
    elif callback.data == '5 pillars':
        return await callback.answer(text='5 pillars')
    elif callback.data == 'select sort':
        return await callback.answer(text='select sort')
    elif callback.data == 'quick sort':
        return await callback.answer(text='quick sort')
    elif callback.data == 'counting sort':
        return await callback.answer(text='counting sort')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)