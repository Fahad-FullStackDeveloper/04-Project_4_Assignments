import pandas as pd
from database import get_total_income, get_total_expenses, get_balance

# Format currency values
def format_currency(value):
    return f"PKR{value:,.2f}"

# Convert database data into a DataFrame
def fetch_dataframe(data, columns):
    return pd.DataFrame(data, columns=columns)

# Get total amount (income or expenses)
def get_total_amount(data):
    df = fetch_dataframe(data, ["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
    return df["Amount"].sum() if not df.empty else 0

# Group data by category and subcategory
def group_by_category(data):
    df = fetch_dataframe(data, ["ID", "Date", "Category", "Subcategory", "Amount", "Description"])
    return df.groupby(["Category", "Subcategory"])["Amount"].sum().reset_index() if not df.empty else pd.DataFrame()
