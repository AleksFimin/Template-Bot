from aiogram import types, exceptions


async def delete_messsage(message: types.Message):
    try:
        await message.delete()
    except (
        exceptions.MessageCantBeDeleted,
        exceptions.MessageToDeleteNotFound
    ):
        pass


async def edit_text_or_answer(*args, **kwargs):
    message = args[0]
    message: types.Message

    try:
        await message.edit_text(**kwargs)
    except (
        exceptions.MessageCantBeEdited, exceptions.MessageTextIsEmpty,
        exceptions.MessageNotModified, exceptions.MessageToEditNotFound
    ):
        await message.answer(**kwargs)