from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_keyboard_modules = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. Алгоритмы в программировании', callback_data='Algorithms')],
                     [InlineKeyboardButton(text='2. Основы сетевого взаимодействия.', callback_data='TCP/IP')],
                     [InlineKeyboardButton(text='3. Python. Полезные модули.', callback_data='Python')],
                     [InlineKeyboardButton(text='4. Многопоточность.', callback_data='Multithreading')]],
    row_width=1)

inline_keyboard_algorithms = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. Сложность алгоритма', callback_data='algorithm complexity')],
                     [InlineKeyboardButton(text='2. Пять столпов асимптотической оценки сложности', callback_data='5 pillars')],
                     [InlineKeyboardButton(text='3. Сортировка выбором', callback_data='select sort')],
                     [InlineKeyboardButton(text='4. Быстрая сортировка', callback_data='quick sort')],
                     [InlineKeyboardButton(text='5. Сортировка подсчетом', callback_data='counting sort')],
                     [InlineKeyboardButton(text='Закрыть', callback_data='close')]],
    row_width=1)

inline_keyboard_TCP = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. ', callback_data='algorithm complexity')],
                     [InlineKeyboardButton(text='2. ', callback_data='5 pillars')],
                     [InlineKeyboardButton(text='3. ', callback_data='select sort')],
                     [InlineKeyboardButton(text='4. ', callback_data='quick sort')],
                     [InlineKeyboardButton(text='5. ', callback_data='counting sort')],
                     [InlineKeyboardButton(text='Закрыть', callback_data='close')]],
    row_width=1)

inline_keyboard_python = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. ', callback_data='algorithm complexity')],
                     [InlineKeyboardButton(text='2. ', callback_data='5 pillars')],
                     [InlineKeyboardButton(text='3. ', callback_data='select sort')],
                     [InlineKeyboardButton(text='4. ', callback_data='quick sort')],
                     [InlineKeyboardButton(text='5. ', callback_data='counting sort')],
                     [InlineKeyboardButton(text='Закрыть', callback_data='close')]],
    row_width=1)

inline_keyboard_multithreading = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='1. ', callback_data='algorithm complexity')],
                     [InlineKeyboardButton(text='2. ', callback_data='5 pillars')],
                     [InlineKeyboardButton(text='3. ', callback_data='select sort')],
                     [InlineKeyboardButton(text='4. ', callback_data='quick sort')],
                     [InlineKeyboardButton(text='5. ', callback_data='counting sort')],
                     [InlineKeyboardButton(text='Закрыть', callback_data='close')]],
    row_width=1)
