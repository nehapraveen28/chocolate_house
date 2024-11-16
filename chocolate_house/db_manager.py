import sqlite3

DB_PATH = "db/chocolate.db"

def initialize_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT,
            availability BOOLEAN,
            start_date DATE,
            end_date DATE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT,
            quantity INTEGER,
            unit TEXT,
            last_updated DATETIME
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            flavor_suggestion TEXT,
            allergy_concern TEXT
        )
    """)
    connection.commit()
    connection.close()
    print("Database initialized successfully.")

# Ensure this line is included to call the function
if __name__ == "__main__":
    initialize_db()
