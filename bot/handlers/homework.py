from aiogram import types
from bot.database.db import cursor, commit

async def add_homework(message: types.Message):
    _, task, deadline = message.text.split(";")
    cursor.execute(
        "INSERT INTO homework (user_id, task, deadline) VALUES (?, ?, ?)",
        (message.from_user.id, task, deadline)
    )
    commit()
    await message.answer("📝 Домашка добавлена")
