from .db import cursor, commit

cursor.executescript("""
CREATE TABLE IF NOT EXISTS schedule(
    user_id INTEGER,
    subject TEXT,
    time TEXT
);

CREATE TABLE IF NOT EXISTS homework(
    user_id INTEGER,
    task TEXT,
    deadline TEXT,
    done INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS goals(
    user_id INTEGER,
    goal TEXT,
    progress INTEGER DEFAULT 0
);
""")

commit()
