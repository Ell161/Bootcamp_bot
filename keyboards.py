from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

inline_keyboard_modules = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. Алгоритмы в программировании', callback_data='Algorithms')],
                     [InlineKeyboardButton(text='2. Основы сетевого взаимодействия.', callback_data='TCP/IP')],
                     [InlineKeyboardButton(text='3. Python. Полезные модули.', callback_data='Python')],
                     [InlineKeyboardButton(text='4. Многопоточность.', callback_data='Multithreading')]],
    row_width=1)

inline_keyboard_algorithms = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. Сложность алгоритма', callback_data='algorithm complexity')],
                     [InlineKeyboardButton(text='2. Пять столпов асимптотической оценки сложности', callback_data='pillars')],
                     [InlineKeyboardButton(text='3. Сортировка выбором', callback_data='select sort')],
                     [InlineKeyboardButton(text='4. Сортировка пузырьком', callback_data='bubble sort')],
                     [InlineKeyboardButton(text='5. Быстрая сортировка', callback_data='quick sort')],
                     [InlineKeyboardButton(text='6. Сортировка подсчетом', callback_data='counting sort')],
                     [InlineKeyboardButton(text='⬆️ Закрыть ⬆️', callback_data='close')]],
    row_width=1)

inline_keyboard_python = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. Flask', callback_data='flask')],
                     [InlineKeyboardButton(text='2. Jinja', callback_data='jinja')],
                     [InlineKeyboardButton(text='3. Turtle', callback_data='turtle')],
                     [InlineKeyboardButton(text='4. Requests', callback_data='requests')],
                     [InlineKeyboardButton(text='5. SQLite3', callback_data='sqlite')],
                     [InlineKeyboardButton(text='⬆️ Закрыть ⬆️', callback_data='close')]],
    row_width=1)

inline_keyboard_close = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='⬆️ Закрыть ⬆️', callback_data='close')]],
    row_width=1)
