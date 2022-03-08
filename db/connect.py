from data.config import *
import aiomysql

async def create_pool():
    pool = await aiomysql.create_pool(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        port=PORT,
        autocommit=AUTOCOMMIT
    )
    return pool

async def close_pool(pool: aiomysql.Pool):
    pool.close()
    await pool.wait_closed()