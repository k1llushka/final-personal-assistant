from bot.database.db import cursor, commit

def update_progress(user_id, goal, value):
    cursor.execute(
        "UPDATE goals SET progress=? WHERE user_id=? AND goal=?",
        (value, user_id, goal)
    )
    commit()
