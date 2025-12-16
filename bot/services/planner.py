from bot.database.db import cursor

def get_today_schedule(user_id):
    cursor.execute(
        "SELECT subject, time FROM schedule WHERE user_id=? ORDER BY time",
        (user_id,)
    )
    return cursor.fetchall()


def get_pending_homework(user_id):
    cursor.execute(
        "SELECT task, deadline FROM homework WHERE user_id=? AND done=0",
        (user_id,)
    )
    return cursor.fetchall()
