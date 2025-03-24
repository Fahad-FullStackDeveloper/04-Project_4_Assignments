import sqlite3

DB_NAME = "budget.db"

def init_db():
    """Initialize the database and create tables if they do not exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        subcategory TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        source TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT
    )""")

    conn.commit()
    conn.close()

def add_expense(date, category, subcategory, amount, description):
    """Insert an expense record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, category, subcategory, amount, description) VALUES (?, ?, ?, ?, ?)",
              (date, category, subcategory, float(amount), description))
    conn.commit()
    conn.close()

def add_income(date, source, amount, description):
    """Insert an income record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO income (date, source, amount, description) VALUES (?, ?, ?, ?)",
              (date, source, float(amount), description))
    conn.commit()
    conn.close()

def get_expenses():
    """Retrieve all expenses from the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    return data

def get_income():
    """Retrieve all income from the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM income ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    return data

def update_expense(expense_id, date, category, subcategory, amount, description):
    """Update an expense record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    UPDATE expenses SET date=?, category=?, subcategory=?, amount=?, description=? WHERE id=?
    """, (date, category, subcategory, float(amount), description, expense_id))
    conn.commit()
    conn.close()

def update_income(income_id, date, source, amount, description):
    """Update an income record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    UPDATE income SET date=?, source=?, amount=?, description=? WHERE id=?
    """, (date, source, float(amount), description, income_id))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    """Delete an expense record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

def delete_income(income_id):
    """Delete an income record."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM income WHERE id=?", (income_id,))
    conn.commit()
    conn.close()
