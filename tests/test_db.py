import unittest
import os
import sqlite3

# ВАЖНО: импорт создаёт таблицы
import bot.database.models

DB_PATH = "study.db"


class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Подключение к базе перед каждым тестом"""
        self.assertTrue(
            os.path.exists(DB_PATH),
            "Файл базы данных study.db не найден"
        )
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_tables_created(self):
        """Проверка, что все таблицы существуют"""
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        tables = [row[0] for row in self.cursor.fetchall()]

        self.assertIn("schedule", tables)
        self.assertIn("homework", tables)
        self.assertIn("goals", tables)

    def test_insert_and_select_goal(self):
        """Проверка вставки и чтения данных"""
        self.cursor.execute(
            "INSERT INTO goals (user_id, goal, progress) VALUES (?, ?, ?)",
            (1, "CI Test Goal", 75)
        )
        self.conn.commit()

        self.cursor.execute(
            "SELECT goal, progress FROM goals WHERE user_id=1"
        )
        goal, progress = self.cursor.fetchone()

        self.assertEqual(goal, "CI Test Goal")
        self.assertEqual(progress, 75)


if __name__ == "__main__":
    unittest.main()
