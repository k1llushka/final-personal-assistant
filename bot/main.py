from aiogram import Bot, Dispatcher, executor, types
from bot.config import BOT_TOKEN
from bot.ui.keyboards import main_kb
from bot.handlers import schedule, homework, goals, analytics
import bot.database.models
from bot.handlers import progress
from bot.handlers.start import start_handler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🎓 Учебный помощник запущен", reply_markup=main_kb)

dp.register_message_handler(schedule.add_lesson, commands=["schedule"])
dp.register_message_handler(homework.add_homework, commands=["homework"])
dp.register_message_handler(goals.add_goal, commands=["goal"])
dp.register_message_handler(analytics.analytics, commands=["analytics"])
dp.register_message_handler(progress.show_progress, commands=["progress"])
dp.register_message_handler(start_handler, commands=["start"])

if __name__ == "__main__":
    executor.start_polling(dp)
