import sqlite3

DB_NAME = "pet_adoption.db"

class DB:
    @staticmethod
    def get_connection():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def execute(query, params=()):
        conn = DB.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

# ---------- Initialize Tables ----------
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create shelters table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shelters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)

    # Create pets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            age INTEGER NOT NULL CHECK(age >= 0),
            shelter_id INTEGER NOT NULL,
            FOREIGN KEY (shelter_id) REFERENCES shelters(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()
