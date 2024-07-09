
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
import logging
import asyncio
import config

# Экземпляр
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


start_message2 = "Этот бот создан для комфортного взаимодействия джунов и менторов внутри команды. Мы уверены, что Менторинг бот станет незаменимым инструментом для развития вашей команды и повышения эффективности менторинга! \n\n\nДля начала выберете свой функционал"
message_for_jun = "🧭 Найдите свой путь. Менторинг бот поможет вам ориентироваться в образовательном треке, отслеживать свой прогресс, не пропустить важные этапы и получать обратную связь"
message_for_mentr = "🚀 Создайте пространство для успеха. Менторинг бот поможет вам организовать и оптимизировать процесс обучения джунов. Добавляйте участников, назначайте задачи, отслеживайте прогресс и получайте обратную связь"
welcome_mentor_message = "Добро пожаловать, Ментор! Теперь вам предстоит создать пространство команды и загрузить базу знаний"
ground_of_jun = "Добро пожаловать! Введи код пространства, которое создал для тебя твой ментор"
messafe_about_of_bot  = "Этот бот создан для комфортного взаимодействия джунов и менторов внутри команды. \n  Мы уверены, что Менторинг бот станет незаменимым инструментом для развития вашей команды и повышения эффективности менторинга!"

async def handler_start(message: types.Message):
    tg_channel_btn = InlineKeyboardButton(
        text="Я джун",
        callback_data='jun',
    )
    tg_channel_btn2 = InlineKeyboardButton(
        text="Я ментор",
        callback_data='mentor',
    )
    row = [tg_channel_btn, tg_channel_btn2]
    rows = [row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    sent_message2 = await message.answer(
        text=start_message2,
        reply_markup=markup,
    )
    return sent_message2.message_id

async def handler_ment(callback_query: CallbackQuery):
    start_button = InlineKeyboardButton(
        text="Вернуться к началу",
        callback_data='start',
    )
    continue_btn = InlineKeyboardButton(
        text="Продолжить",
        callback_data='continue_mentor',
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[start_button, continue_btn]])
    await callback_query.message.answer(message_for_mentr, reply_markup=markup)
    await callback_query.message.delete()  # Удаление сообщения
    await callback_query.answer()


async def handler_jun(callback_query: CallbackQuery):
    start_button = InlineKeyboardButton(
        text="Вернуться к началу",
        callback_data='start',
    )
    continue_btn = InlineKeyboardButton(
        text="Продолжить",
        callback_data='continue_jun',
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[start_button, continue_btn]])
    await callback_query.message.answer(message_for_jun, reply_markup=markup)
    await callback_query.message.delete()  # Удаление сообщения
    await callback_query.answer()
# Пространство Ментора

async def handler_continue_callback_mentor(callback_query: CallbackQuery):
    start_button = InlineKeyboardButton(
        text="Вернуться",
        callback_data='mentor',
    )
    begin_button = InlineKeyboardButton(
        text="Начать",
        callback_data='begin_mentor',
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[start_button, begin_button]])
    await callback_query.message.answer(welcome_mentor_message, reply_markup=markup)
    await callback_query.message.delete()
    await callback_query.answer()

async def handler_begin_mentor(callback_query: CallbackQuery):
    ground_of_command_btn = KeyboardButton(
        text="Пространство команды"
    )
    my_juns_btn = KeyboardButton(
        text="Мои джуны"
    )
    baza_znanie_btn = KeyboardButton(
        text="База знаний"
    )
    my_profile_btn = KeyboardButton(
        text="Мой профиль"
    )
    about_of_bot_btn = KeyboardButton(
        text="О боте"
    )
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [ground_of_command_btn],
            [my_juns_btn],
            [baza_znanie_btn],
            [my_profile_btn],
            [about_of_bot_btn]
        ],
        resize_keyboard=True
    )

    await callback_query.message.answer("Назовите рабочее пространство", reply_markup=markup)
    await callback_query.message.delete()
    await callback_query.answer()

# Пространство Джуна
async def handler_continue_callback_jun(callback_query: CallbackQuery):
    ground_of_command_btn = KeyboardButton(
        text="Пространство команды"
    )
    baza_znanie_btn = KeyboardButton(
        text="База знаний"
    )
    svyz_s_mentron_btn = KeyboardButton(
        text="Связь с ментором"
    )
    my_profile_btn = KeyboardButton(
        text="Мой профиль"
    )
    about_of_bot_btn = KeyboardButton(
        text="О боте"
    )
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [ground_of_command_btn],
            [baza_znanie_btn],
            [svyz_s_mentron_btn],
            [my_profile_btn],
            [about_of_bot_btn]
        ],
        resize_keyboard=True
    )

    await callback_query.message.answer(ground_of_jun, reply_markup=markup)
    await callback_query.message.delete()
    await callback_query.answer()

async def handler_ground_of_command(message: types.Message):
    await message.answer("Пространство команды", reply_markup=ReplyKeyboardRemove())

async def handler_baza_znanie(message: types.Message):
    await message.answer("База знаний", reply_markup=ReplyKeyboardRemove())

async def handler_svyz_s_mentron(message: types.Message):
    await message.answer("Связь с ментором", reply_markup=ReplyKeyboardRemove())

async def handler_my_profile(message: types.Message):
    await message.answer("Мой профиль", reply_markup=ReplyKeyboardRemove())

# О боте
async def handler_about_of_bot(message: types.Message):
    await message.answer("О боте", reply_markup=ReplyKeyboardRemove())
    await message.answer(messafe_about_of_bot)
    

async def handler_start_callback(callback_query: CallbackQuery):
    await callback_query.message.delete()  # Удаление сообщения
    await handler_start(callback_query.message)

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.message.register(handler_start, CommandStart())
    # Регистрация для ментра
    dp.callback_query.register(handler_ment, lambda c: c.data == 'mentor')
    # Регистрация для джуна
    dp.callback_query.register(handler_jun, lambda c: c.data == 'jun')
    # Регистрация начального меню
    dp.callback_query.register(handler_start_callback, lambda c: c.data == 'start')
    # Про-во ментора
    dp.callback_query.register(handler_continue_callback_mentor, lambda c: c.data == 'continue_mentor')
    dp.callback_query.register(handler_begin_mentor, lambda c: c.data == 'begin_mentor')
    # Про-во джуна
    dp.callback_query.register(handler_continue_callback_jun, lambda c: c.data == 'continue_jun')
    # Регистрация пр-ва команды
    dp.message.register(handler_ground_of_command, lambda message: message.text == "Пространство команды")
    # Регистрация базы знаний
    dp.message.register(handler_baza_znanie, lambda message: message.text == "База знаний")
    # Регистрация связи с ментором
    dp.message.register(handler_svyz_s_mentron, lambda message: message.text == "Связь с ментором")
    # Регистрация профиля
    dp.message.register(handler_my_profile, lambda message: message.text == "Мой профиль")
    # Регистрация о боте
    dp.message.register(handler_about_of_bot, lambda message: message.text == "О боте")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())