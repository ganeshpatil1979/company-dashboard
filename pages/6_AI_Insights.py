import streamlit as st

from utils.data_loader import load_data

df = load_data()

st.title("🤖 AI Insights")

highest_sales = df.loc[
    df["Sales ($B)"].idxmax()
]

highest_profit = df.loc[
    df["Profit ($B)"].idxmax()
]

highest_market = df.loc[
    df["Market Value ($B)"].idxmax()
]

st.success(
f"""
Top Revenue Company

{highest_sales['Company']}

Revenue:
${highest_sales['Sales ($B)']:.2f}B
"""
)

st.info(
f"""
Top Profit Company

{highest_profit['Company']}

Profit:
${highest_profit['Profit ($B)']:.2f}B
"""
)

st.warning(
f"""
Highest Market Value

{highest_market['Company']}

Market Value:
${highest_market['Market Value ($B)']:.2f}B
"""
)