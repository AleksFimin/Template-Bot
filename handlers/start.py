from loader import dp, Cursor
from aiogram import types
from utils import mysql
from utils.quick_method import edit_text_or_answer


@dp.message_handler()
@mysql.cursor_handler
async def start(message: types.Message, cur=Cursor):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('ss', callback_data='sess'))
    await message.answer(message.text, reply_markup=markup)


@dp.callback_query_handler()
async def c(callback):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('sss', callback_data='sess'))

    text = 'Hi Guyssssssssss'
    await edit_text_or_answer(callback.message, text=text, reply_markup=markup)