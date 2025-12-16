import matplotlib.pyplot as plt
from bot.database.db import cursor

def build_progress_chart(user_id):
    cursor.execute(
        "SELECT goal, progress FROM goals WHERE user_id=?",
        (user_id,)
    )
    data = cursor.fetchall()

    if not data:
        return None

    goals = [g[0] for g in data]
    progress = [g[1] for g in data]

    plt.figure()
    plt.bar(goals, progress)
    plt.title("Прогресс целей")
    plt.ylabel("Проценты")
    plt.ylim(0, 100)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    path = f"progress_{user_id}.png"
    plt.savefig(path)
    plt.close()

    return path
