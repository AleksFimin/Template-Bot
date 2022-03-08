from loader import dp
from aiogram.types import ChatMemberUpdated


@dp.my_chat_member_handler()
async def my_chat_member_private(update: ChatMemberUpdated):
    if update.chat.type != 'private':
        pass

    if update.new_chat_member.status == 'member':
        pass

    if update.new_chat_member.status == 'left':
        pass