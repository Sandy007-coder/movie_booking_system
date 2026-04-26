import sqlite3
import os

# Ensure folder exists
DATA_PATH = os.path.join(os.getcwd(), "data_storage")
os.makedirs(DATA_PATH, exist_ok=True)

DB_PATH = os.path.join(DATA_PATH, "bookings.db")


def connect():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    # ----------------------------
    # CHECK IF TABLE EXISTS
    # ----------------------------
    cursor.execute("""
    SELECT name FROM sqlite_master 
    WHERE type='table' AND name='bookings'
    """)
    table_exists = cursor.fetchone()

    if table_exists:
        # ----------------------------
        # CHECK COLUMNS (important fix)
        # ----------------------------
        cursor.execute("PRAGMA table_info(bookings)")
        columns = [col[1] for col in cursor.fetchall()]

        # If seats column missing → reset table
        if "seats" not in columns:
            print("⚠️ Updating database schema...")
            cursor.execute("DROP TABLE bookings")

    # ----------------------------
    # CREATE TABLE (final schema)
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id TEXT,
        city TEXT,
        theatre TEXT,
        movie TEXT,
        screen TEXT,
        time TEXT,
        tickets INTEGER,
        seats TEXT
    )
    """)

    conn.commit()
    conn.close()