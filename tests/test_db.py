import unittest
import sqlite3
import os

DB_PATH = "study.db"


class TestDatabase(unittest.TestCase):

    def test_database_file_exists(self):
        """Проверка, что файл базы данных существует"""
        self.assertTrue(
            os.path.exists(DB_PATH),
            "Файл базы данных study.db не найден"
        )

    def test_tables_created(self):
        """Проверка наличия всех таблиц"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        tables = [row[0] for row in cursor.fetchall()]

        conn.close()

        self.assertIn("schedule", tables)
        self.assertIn("homework", tables)
        self.assertIn("goals", tables)

    def test_insert_and_select_goal(self):
        """Проверка вставки и чтения данных"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO goals (user_id, goal, progress) VALUES (?, ?, ?)",
            (999, "Тестовая цель", 50)
        )
        conn.commit()

        cursor.execute(
            "SELECT goal, progress FROM goals WHERE user_id=?",
            (999,)
        )
        result = cursor.fetchone()

        conn.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Тестовая цель")
        self.assertEqual(result[1], 50)


if __name__ == "__main__":
    unittest.main()
