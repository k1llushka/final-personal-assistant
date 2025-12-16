# 🎓 Study Helper Telegram Bot

Учебный Telegram-бот с удобным пайплайном через GitHub.

## 🚀 Возможности
- 📅 Планировщик расписания пар
- 📝 Учёт домашних заданий
- 🎯 Трекер целей с прогрессом
- 📊 Аналитика обучения
- 📈 Графики прогресса
- 🔁 CI pipeline через GitHub Actions

## 🧱 Архитектура
Проект построен по модульной архитектуре:
- handlers — логика команд
- services — аналитика и отчёты
- database — хранение данных
- ui — кнопки и интерфейс
- .github/workflows — CI pipeline

## 📦 Установка
```bash
git clone https://github.com/username/study-helper-bot.git
cd study-helper-bot
pip install -r requirements.txt
