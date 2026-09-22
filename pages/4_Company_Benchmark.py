import streamlit as st
import pandas as pd

from utils.data_loader import load_data

# Load data
df = load_data()

# Clean column names
df.columns = df.columns.str.strip()

st.title("🎯 Company Benchmark")

# Required columns
metric_columns = [
    "Sales ($B)",
    "Profit ($B)",
    "Assets ($B)",
    "Market Value ($B)"
]

required_columns = ["Company", "Industry"] + metric_columns

# Check that all required columns exist
missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error("The following columns are missing from your data:")
    st.write(missing_columns)

    st.info("Available columns in your dataset:")
    st.write(df.columns.tolist())

    st.stop()

# Company selection
companies = sorted(df["Company"].dropna().unique())

company = st.selectbox(
    "Company",
    companies
)

# Selected company
selected = df[df["Company"] == company].iloc[0]

# Filter companies from the same industry
industry_df = df[
    df["Industry"] == selected["Industry"]
]

# Calculate industry averages
industry_avg = industry_df[metric_columns].mean()

# Create comparison table
comparison = pd.DataFrame({
    "Metric": [
        "Sales",
        "Profit",
        "Assets",
        "Market Value"
    ],
    company: [
        selected["Sales ($B)"],
        selected["Profit ($B)"],
        selected["Assets ($B)"],
        selected["Market Value ($B)"]
    ],
    "Industry Average": [
        industry_avg["Sales ($B)"],
        industry_avg["Profit ($B)"],
        industry_avg["Assets ($B)"],
        industry_avg["Market Value ($B)"]
    ]
})

# Display
st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)