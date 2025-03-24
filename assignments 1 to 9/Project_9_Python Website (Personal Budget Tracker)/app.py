import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import (
    init_db, add_expense, add_income, get_expenses, get_income,
    update_expense, update_income, delete_expense, delete_income
)

# ✅ **Application Metadata**
APP_VERSION = "1.3.0"
DEVELOPER_NAME = "Fahad Khakwani"
DEVELOPER_CONTACT = "fahadyousufkhakwani@gmail.com"
GITHUB_REPO = "https://github.com/Fahad-FullStackDeveloper/04-Project_4_Assignments/tree/main/assignments%201%20to%209/Project_9_Python%20Website%20(Personal%20Budget%20Tracker)"

# ✅ **Initialize Database**
init_db()

st.title("💰 Personal Budget Tracker (Income & Expenses)")
st.caption(f"Version {APP_VERSION} | Developed by {DEVELOPER_NAME} | 📧 {DEVELOPER_CONTACT}")

# Sidebar Navigation
menu = st.sidebar.radio("📌 Menu", ["View Summary", "Add Income", "Add Expense", "About"])

# ✅ **Add Expense Section**
if menu == "Add Expense":
    st.sidebar.subheader("📉 Add a New Expense")
    date = st.sidebar.date_input("Date")
    category = st.sidebar.selectbox("Category", [
    "Essentials", 
    "Transportation", 
    "Utilities & Bills", 
    "Financial & Savings", 
    "Food & Dining", 
    "Shopping & Personal", 
    "Education & Learning", 
    "Entertainment & Leisure", 
    "Travel & Vacation", 
    "Family & Childcare", 
    "Home & Furniture", 
    "Giving & Donations", 
    "Miscellaneous"
    ])
    # Subcategories based on the main category
    subcategories = {
    "Essentials": ["Grocery", "Supermarket", "Health", "Medical Bills", "Pharmacy", "Doctor Consultation", "Rent", "Mortgage", "Home Maintenance", "Property Taxes"],
    "Transportation": ["Bike", "Bike Fuel", "Bike Maintenance", "Car", "Car Fuel", "Car Maintenance", "Parking", "Public Transport", "Ride Sharing (Uber, Lyft)", "Airfare", "Train & Bus Tickets"],
    "Utilities & Bills": ["Electricity", "Water", "Gas", "Phone & Internet", "Cable TV", "Streaming Services (Netflix, Spotify)"],
    "Financial & Savings": ["Insurance (Car, Home, Health, Life)", "Loans (Car, Student, Home)", "Savings", "Investment", "Retirement Contribution", "Credit Card Payments", "Debt Repayment", "Taxes"],
    "Food & Dining": ["Restaurants", "Fast Food", "Coffee", "Takeout & Delivery", "Bars & Alcohol"],
    "Shopping & Personal": ["Clothing", "Shoes", "Accessories", "Jewelry", "Beauty & Cosmetics", "Hair & Salon", "Spa & Massage", "Gym Membership", "Sports & Fitness Equipment"],
    "Education & Learning": ["School Fees", "College Tuition", "Books & Stationery", "Online Courses", "Workshops & Seminars"],
    "Entertainment & Leisure": ["Movies", "Concerts & Events", "Amusement Parks", "Gaming", "Hobbies", "Toys & Games"],
    "Travel & Vacation": ["Hotels", "Flights", "Rental Cars", "Tourist Attractions", "Luggage & Travel Gear"],
    "Family & Childcare": ["Childcare", "Baby Supplies", "School Activities", "Elderly Care", "Pet Food", "Veterinary Bills"],
    "Home & Furniture": ["Furniture", "Appliances", "Home Décor", "Cleaning Supplies", "Gardening", "Security System"],
    "Giving & Donations": ["Charity", "Religious Contributions", "Gifts", "Celebrations & Parties"],    
    "Miscellaneous": ["Emergency Fund", "Unexpected Expenses", "Miscellaneous"]
    }

    # Display subcategories based on selected category
    subcategory = st.sidebar.selectbox("Subcategory", subcategories.get(category, ["Select a Category First"]))
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

# ✅ **View Summary Section (WITH BAR CHARTS & GRAPH CHARTS)**
elif menu == "View Summary":
    st.subheader("📊 Budget Summary")
    
    expenses = get_expenses()
    income = get_income()
    
    total_expense = sum([x[4] for x in expenses]) if expenses else 0
    total_income = sum([x[3] for x in income]) if income else 0
    balance = total_income - total_expense

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="💸 Total Income", value=f"Rs.{total_income:.2f}")
    with col2:
        st.metric(label="🛒 Total Expenses", value=f"Rs.{total_expense:.2f}")
    with col3:
        st.metric(label="💰 Balance", value=f"Rs.{balance:.2f}")

    # User selection for chart type
    chart_type = st.selectbox("📈 Select Chart Type", ["Bar Chart", "Line Chart"])

    # ✅ **Bar Chart: Expenses by Category**
    if expenses:
        df_exp = pd.DataFrame(expenses, columns=["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
        category_totals = df_exp.groupby("Category")["Amount"].sum().reset_index()
        st.subheader("📉 Expenses by Category")
        if chart_type == "Bar Chart":
            st.bar_chart(category_totals.set_index("Category"))
        else:
            st.line_chart(category_totals.set_index("Category"))

    # ✅ **Bar Chart: Income vs. Expenses**
    if income and expenses:
        summary_data = pd.DataFrame({
            "Type": ["Income", "Expenses"],
            "Amount": [total_income, total_expense]
        })
        st.subheader("📊 Income vs. Expenses")
        if chart_type == "Bar Chart":
            st.bar_chart(summary_data.set_index("Type"))
        else:
            st.line_chart(summary_data.set_index("Type"))

    # ✅ **Monthly Income & Expenses Chart**
    if income or expenses:
        df_income = pd.DataFrame(income, columns=["ID", "Date", "Source", "Amount", "ExtraColumn"]) # Adjust as needed
        df_exp = pd.DataFrame(expenses, columns=["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
        
        # Convert 'Date' columns to datetime format
        df_income["Date"] = pd.to_datetime(df_income["Date"])
        df_exp["Date"] = pd.to_datetime(df_exp["Date"])
        
        # Group data by Month-Year
        df_income["Month"] = df_income["Date"].dt.strftime("%Y-%m")
        df_exp["Month"] = df_exp["Date"].dt.strftime("%Y-%m")
        
        income_monthly = df_income.groupby("Month")["Amount"].sum().reset_index()
        expense_monthly = df_exp.groupby("Month")["Amount"].sum().reset_index()

        # Merge income and expense data
        monthly_summary = pd.merge(income_monthly, expense_monthly, on="Month", how="outer").fillna(0)
        monthly_summary.columns = ["Month", "Income", "Expenses"]
        monthly_summary = monthly_summary.sort_values("Month")

        # Plot Chart based on user selection
        st.subheader("📆 Monthly Income & Expenses")
        if chart_type == "Bar Chart":
            st.bar_chart(monthly_summary.set_index("Month"))
        else:
            st.line_chart(monthly_summary.set_index("Month"))

# ✅ **About Page**
elif menu == "About":
    st.subheader("ℹ️ About This Application")
    st.write("This is a **Personal Budget & Expense Tracker** built using Python and Streamlit.")

    st.markdown(f"""
    - **Version:** {APP_VERSION}  
    - **Developer:** [{DEVELOPER_NAME}](mailto:fahadyousufkhakwani@gmail.com)  
    - **GitHub Repository:** [{GITHUB_REPO}]({GITHUB_REPO})  
    - **Features:**  
        ✅ Add, edit, and delete income and expenses  
        ✅ View financial summary with bar charts  
        ✅ Interactive data tables for editing transactions  
    """)

    # 📢 Version History
    st.subheader("📢 Version History")
    version_history = {
        "1.3.0": [
            "📊 Month-wise Income & Expense Charts",
            "📈 Graph Chart Selection for Visualization",
            "🛠️ Performance Improvements & Bug Fixes"
        ],
        "1.2.0": [
            "🔹 New Categories & Subcategories for Expenses",
            "🔹 Editable Tables for Income & Expenses",
            "🔹 Enhanced UI & Sidebar Form"
        ],
        "1.1.0": [
            "🔹 Updated title to 'Personal Budget Tracker (Income & Expenses)'",
            "🔹 Bar Chart for Financial Summary"
        ],
        "1.0.0": [
            "🎉 Initial version with Add/Delete Expenses & Income"
        ]
    }

    for version, changes in version_data:
        st.markdown(f"**Version {version}**")
        for change in changes:
            st.markdown(f"- {change}")

    # 👨‍💻 Developer Information
    st.subheader("👨‍💻 Developer Information")
    st.markdown(f"""
    - **Developer:** Fahad Khakwani  
    - **Email:** [fahadyousufkhakwani@gmail.com](mailto:fahadyousufkhakwani@gmail.com)  
    - **GitHub Repository:** [Expense Tracker Repo]({GITHUB_REPO})  
    - **Version:** 1.3.0  
    """)
