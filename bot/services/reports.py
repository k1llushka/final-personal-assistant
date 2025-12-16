from bot.database.db import cursor

def generate_report(user_id):
    cursor.execute(
        "SELECT task, deadline FROM homework WHERE user_id=?",
        (user_id,)
    )

    rows = cursor.fetchall()
    report = "📄 Учебный отчёт:\n"

    for task, deadline in rows:
        report += f"• {task} (до {deadline})\n"

    return report
