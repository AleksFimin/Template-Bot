from loader import *
from handlers import __init__
# from middlewares import __init__

async def on_startup(dp):
    dp.pool = await create_pool()
    # await create_tables(dp)


async def on_shutdown(dp):
    await close_pool(dp.pool)


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=False,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        allowed_updates=ALLOWED_UPDATES if ALLOWED_UPDATES else None
    )