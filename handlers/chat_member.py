from loader import dp
from aiogram.types import ChatMemberUpdated


@dp.chat_member_handler()
async def chat_member_update(chat_member: ChatMemberUpdated):
    pass