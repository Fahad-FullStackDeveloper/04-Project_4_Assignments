import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import (
    init_db, add_expense, add_income, get_expenses, get_income,
    update_expense, update_income, delete_expense, delete_income
)

# ✅ **Application Metadata**
APP_VERSION = "1.1.0"
DEVELOPER_NAME = "Fahad Khakwani"
DEVELOPER_CONTACT = "fahadkhakwani.dev@gmail.com"
GITHUB_REPO = "https://github.com/fahadkhakwani/expense-tracker"

# ✅ **Initialize Database**
init_db()

st.title("💰 Personal Budget Tracker (Income & Expenses)")
st.caption(f"Version {APP_VERSION} | Developed by {DEVELOPER_NAME} | 📧 {DEVELOPER_CONTACT}")

# Sidebar Navigation
menu = st.sidebar.radio("📌 Menu", ["Add Expense", "Add Income", "View Summary", "About"])

# ✅ **Add Expense Section**
if menu == "Add Expense":
    st.sidebar.subheader("📉 Add a New Expense")
    date = st.sidebar.date_input("Date")
    category = st.sidebar.selectbox("Category", ["Food", "Transport", "Entertainment", "Health", "Other"])
    subcategory = st.sidebar.text_input("Subcategory (Optional)")
    amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.sidebar.text_area("Description")

    if st.sidebar.button("Add Expense"):
        add_expense(str(date), category, subcategory, amount, description)
        st.sidebar.success("Expense added successfully!")

    # Display Editable Expense Table
    st.subheader("💵 Recent Expenses (Editable)")
    expenses = get_expenses()
    
    if expenses:
        df_exp = pd.DataFrame(expenses, columns=["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
        edited_df = st.data_editor(df_exp, num_rows="dynamic", key="expenses_table")

        for index, row in edited_df.iterrows():
            update_expense(row["ID"], row["Date"], row["Category"], row["Subcategory"], row["Amount"], row["Description"])
        
        for index, row in edited_df.iterrows():
            if st.button(f"🗑️ Delete {row['Category']}", key=f"del_exp_{row['ID']}"):
                delete_expense(row["ID"])
                st.warning("Expense deleted!")

# ✅ **Add Income Section**
elif menu == "Add Income":
    st.sidebar.subheader("📈 Add New Income")
    date = st.sidebar.date_input("Date")
    source = st.sidebar.text_input("Income Source")
    amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.sidebar.text_area("Description")

    if st.sidebar.button("Add Income"):
        add_income(str(date), source, amount, description)
        st.sidebar.success("Income added successfully!")

    # Display Editable Income Table
    st.subheader("💰 Recent Income (Editable)")
    income = get_income()
    
    if income:
        df_inc = pd.DataFrame(income, columns=["ID", "Date", "Source", "Amount", "Description"])
        edited_df_inc = st.data_editor(df_inc, num_rows="dynamic", key="income_table")

        for index, row in edited_df_inc.iterrows():
            update_income(row["ID"], row["Date"], row["Source"], row["Amount"], row["Description"])

        for index, row in edited_df_inc.iterrows():
            if st.button(f"🗑️ Delete {row['Source']}", key=f"del_inc_{row['ID']}"):
                delete_income(row["ID"])
                st.warning("Income deleted!")

# ✅ **View Summary Section (WITH BAR CHARTS)**
elif menu == "View Summary":
    st.subheader("📊 Budget Summary")
    expenses = get_expenses()
    income = get_income()
    
    total_expense = sum([x[4] for x in expenses]) if expenses else 0
    total_income = sum([x[3] for x in income]) if income else 0
    balance = total_income - total_expense

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="💸 Total Income", value=f"${total_income:.2f}")
    with col2:
        st.metric(label="🛒 Total Expenses", value=f"${total_expense:.2f}")
    with col3:
        st.metric(label="💰 Balance", value=f"${balance:.2f}")

    # ✅ **Bar Chart: Expenses by Category**
    if expenses:
        df_exp = pd.DataFrame(expenses, columns=["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
        category_totals = df_exp.groupby("Category")["Amount"].sum().reset_index()
        st.subheader("📉 Expenses by Category")
        st.bar_chart(category_totals.set_index("Category"))

    # ✅ **Bar Chart: Income vs. Expenses**
    if income and expenses:
        summary_data = pd.DataFrame({
            "Type": ["Income", "Expenses"],
            "Amount": [total_income, total_expense]
        })
        st.subheader("📊 Income vs. Expenses")
        st.bar_chart(summary_data.set_index("Type"))

# ✅ **About Page**
elif menu == "About":
    st.subheader("ℹ️ About This Application")
    st.write("This is a **Personal Budget & Expense Tracker** built using Python and Streamlit.")
    st.markdown(f"""
    - **Version:** {APP_VERSION}  
    - **Developer:** [{DEVELOPER_NAME}](mailto:{DEVELOPER_CONTACT})  
    - **GitHub Repository:** [{GITHUB_REPO}]({GITHUB_REPO})  
    - **Features:**  
        ✅ Add, edit, and delete income and expenses  
        ✅ View financial summary with bar charts  
        ✅ Interactive data tables for editing transactions  
    """)
