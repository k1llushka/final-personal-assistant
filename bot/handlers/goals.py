from aiogram import types
from bot.database.db import cursor, commit

async def add_goal(message: types.Message):
    _, goal = message.text.split(";")
    cursor.execute(
        "INSERT INTO goals (user_id, goal) VALUES (?, ?)",
        (message.from_user.id, goal)
    )
    commit()
    await message.answer("🎯 Цель создана")
