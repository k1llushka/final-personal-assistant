from aiogram import types
from bot.database.db import cursor

async def analytics(message: types.Message):
    uid = message.from_user.id

    cursor.execute("SELECT COUNT(*) FROM homework WHERE user_id=?", (uid,))
    hw = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(progress) FROM goals WHERE user_id=?", (uid,))
    progress = cursor.fetchone()[0] or 0

    await message.answer(
        f"📊 Аналитика:\n"
        f"Домашек: {hw}\n"
        f"Средний прогресс целей: {int(progress)}%"
    )
