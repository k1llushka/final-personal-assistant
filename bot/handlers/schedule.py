from aiogram import types
from bot.database.db import cursor, commit

async def add_lesson(message: types.Message):
    _, subject, time = message.text.split(";")
    cursor.execute(
        "INSERT INTO schedule VALUES (?, ?, ?)",
        (message.from_user.id, subject, time)
    )
    commit()
    await message.answer("📅 Пара добавлена")
