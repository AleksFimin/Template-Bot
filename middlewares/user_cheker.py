from loader import dp, localization, _
from data import conifg
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from db.prepared import get_language, user_is_banned
from aiogram import types


class UserCheker(BaseMiddleware): 
    async def on_pre_process_message(self, message, data: dict):
        state = dp.get_current().current_state()
        is_banned = await user_is_banned(dp.pool, message, state)
        if is_banned:
            raise CancelHandler()

        language = await get_language(dp.pool, message, state)
        if not language:
            text = _(language, 'choose_language')

            markup = types.InlineKeyboardMarkup(row_width=3)
            for language in config.BOT_LANGUAGES:
                language_text = _(language, 'language')
                markup.insert(types.InlineKeyboardButton(language_text, callback_data=f'register {language}'))
            await message.answer(text, reply_markup=markup)
            raise CancelHandler()
        

    async def on_pre_process_callback_query(self, callback, data: dict):
        if 'register' in callback.data:
            return

        state = dp.get_current().current_state()
        is_banned = await user_is_banned(dp.pool, callback, state)
        if is_banned:
            raise CancelHandler()

        language = await get_language(dp.pool, callback, state)
        if not language:
            text = _(language, 'choose_language')

            markup = types.InlineKeyboardMarkup(row_width=3)
            for language in config.BOT_LANGUAGES:
                language_text = _(language, 'language')
                markup.insert(types.InlineKeyboardButton(language_text, callback_data=f'register {language}'))
            await callback.message.answer(text, reply_markup=markup)
            raise CancelHandler()


dp.middleware.setup(UserCheker())