from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add("📅 Расписание", "📝 Домашка")
main_kb.add("🎯 Цели", "📊 Аналитика")
