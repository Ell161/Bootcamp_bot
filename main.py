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
    match callback.data:
        case 'Algorithms':
            photo = open('img/algorithm.jpg', 'rb')
            return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                                 photo=photo, caption=variables.Algorithms, parse_mode='HTML',
                                                 reply_markup=keyboards.inline_keyboard_algorithms)
        case 'TCP/IP':
            photo = open('img/server.jpg', 'rb')
            return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                                 photo=photo, caption=variables.TCP_IP, parse_mode='HTML',
                                                 reply_markup=keyboards.inline_keyboard_close)
        case 'Python':
            photo = open('img/python.jpg', 'rb')
            return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                                 photo=photo, caption=variables.Python, parse_mode='HTML',
                                                 reply_markup=keyboards.inline_keyboard_python)
        case 'Multithreading':
            photo = open('img/multithreading.jpg', 'rb')
            return await callback.bot.send_photo(chat_id=callback.message.chat.id,
                                                 photo=photo, caption=variables.Multithreading, parse_mode='HTML',
                                                 reply_markup=keyboards.inline_keyboard_close)
        case 'algorithm complexity':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.algorithm_complexity, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)
        case 'pillars':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.pillars, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)
        case 'select sort':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.select_sort, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)
        case 'bubble sort':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.bubble_sort, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)
        case 'quick sort':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.quick_sort, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)
        case 'counting sort':
            return await callback.bot.send_message(chat_id=callback.message.chat.id,
                                                   text=variables.counting_sort, parse_mode='HTML',
                                                   reply_markup=keyboards.inline_keyboard_close)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
