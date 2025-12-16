from aiogram import types
from bot.ui.keyboards import main_kb

async def start_handler(message: types.Message):
    await message.answer(
        "🎓 *Учебный помощник*\n\n"
        "Что я умею:\n"
        "📅 Расписание пар\n"
        "📝 Домашние задания\n"
        "🎯 Цели и прогресс\n"
        "📊 Аналитика обучения\n\n"
        "Используй команды или кнопки 👇",
        reply_markup=main_kb,
        parse_mode="Markdown"
    )
