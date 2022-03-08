from loader import dp

def cursor_handler(func):
    arguments = func.__code__.co_varnames
    
    if 'state' in arguments:
        async def set_func(update, state, cursor=None):
            async with dp.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    if 'cur' in arguments:
                        await func(update, state, cursor)
                    else:
                        await func(update, state)
    else:
        async def set_func(update, cursor=None):
            async with dp.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    if 'cur' in arguments:
                        await func(update, cursor)
                        
    return set_func