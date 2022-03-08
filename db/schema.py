import aiomysql

schemas = []

schemas.append('''CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    balance NUMERIC NOT NULL,
    language VARCHAR(10) NOT NULL,
    status TINYINT NOT NULL,
    UNIQUE (user_id)
)''')


async def create_tables(dp):
    async with dp.pool.acquire() as con:
        async with con.cursor() as cursor:
            for schema in schemas:
                await cursor.execute(schema)