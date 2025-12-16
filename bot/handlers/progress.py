from aiogram import types
from bot.services.progress_plot import build_progress_chart

async def show_progress(message: types.Message):
    path = build_progress_chart(message.from_user.id)

    if not path:
        await message.answer("❌ У тебя пока нет целей")
        return

    with open(path, "rb") as img:
        await message.answer_photo(img, caption="📈 Твой прогресс")
