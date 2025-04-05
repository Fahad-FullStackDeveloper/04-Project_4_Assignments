import streamlit as st
import sqlite3
import os
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def create_users_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

def get_user_db(username):
    return f"{username}.db"

def create_budget_db(username):
    db_path = get_user_db(username)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            type TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(username, date, category, amount, type_):
    db_path = get_user_db(username)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, category, amount, type) VALUES (?, ?, ?, ?)", (date, category, amount, type_))
    conn.commit()
    conn.close()

def get_transactions(username):
    db_path = get_user_db(username)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    return transactions

def main():
    st.title("Personal Budget Tracker")
    create_users_db()
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = ""
 
    menu = ["Login", "Register"] if not st.session_state.authenticated else ["Logout", "Budget Tracker"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create a New Account")
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Account created successfully! Please login.")
            else:
                st.error("Username already exists. Try a different one.")
    
    elif choice == "Login":
        st.subheader("User Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                create_budget_db(username)
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
    
    elif choice == "Logout":
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.experimental_rerun()
    
    elif choice == "Budget Tracker":
        st.subheader(f"Welcome, {st.session_state.username}!")
        create_budget_db(st.session_state.username)
        date = st.date_input("Transaction Date")
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        type_ = st.radio("Type", ["Income", "Expense"])
        if st.button("Add Transaction"):
            add_transaction(st.session_state.username, date, category, amount, type_)
            st.success("Transaction added successfully!")
        
        st.subheader("Transaction History")
        transactions = get_transactions(st.session_state.username)
        if transactions:
            for t in transactions:
                st.write(f"{t[1]} - {t[2]}: ${t[3]} ({t[4]})")
        else:
            st.write("No transactions found.")

if __name__ == "__main__":
    main()
