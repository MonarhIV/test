from flask_sqlalchemy import SQLAlchemy
conn = SQLAlchemy()

"""
БД вынесено в отдельный файл для декомпозиции моделей
"""

import psycopg


async def Select(name):
    async with await psycopg.AsyncConnection.connect(f"dbname=test user=postgres password=123") as aconn:
        async with aconn.cursor() as acur:
            try:
                query = "SELECT * FROM device WHERE name ILIKE %s"
                formatted_query = query % ('\'%' + name + '%\'')
                await acur.execute(formatted_query)
                d = await acur.fetchall()
                return d
            except psycopg.errors.UniqueViolation:
                return False