from aiomysql import Pool, Connection, Cursor
from loader import FSMContext


async def get_language(pool: Pool, update, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language')
    user_id = update.from_user.id

    if language is None:
        async with pool.acquire() as conn:
            conn: Connection
            async with conn.cursor() as cursor:
                cursor: Cursor
                query = "SELECT `language` FROM `users` WHERE `user_id` = %s"
                await cursor.execute(query, [user_id])

                if cursor.rowcount > 0:
                    language = await cursor.fetchone()
                    await state.update_data(language=language[0])
                    return language[0]
                return None

    return language


async def user_is_banned(pool: Pool, update, state: FSMContext):
    user_data = await state.get_data()
    is_banned = user_data.get('is_banned')
    user_id = update.from_user.id

    if is_banned is None:
        async with pool.acquire() as conn:
            conn: Connection
            async with conn.cursor() as cursor:
                cursor: Cursor
                query = "SELECT `id` FROM `blacklist` WHERE `user_id` = %s and `is_bot` = %s"
                await cursor.execute(query, [user_id, 0])

                if cursor.rowcount > 0:
                    await state.update_data(is_banned=1)
                    return True

                await state.update_data(is_banned=0)
                return False

    return is_banned