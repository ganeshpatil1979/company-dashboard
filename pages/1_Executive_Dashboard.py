import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📊 Executive Dashboard")

# -----------------------------
# KPI Metrics
# -----------------------------
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Companies", len(df))
c2.metric("Sales", f"${df['Sales ($B)'].sum():,.0f}B")
c3.metric("Profit", f"${df['Profit ($B)'].sum():,.0f}B")
c4.metric("Assets", f"${df['Assets ($B)'].sum():,.0f}B")
c5.metric("Market Value", f"${df['Market Value ($B)'].sum():,.0f}B")


# -----------------------------
# Top 10 Companies by Sales
# -----------------------------
top10 = df.nlargest(10, "Sales ($B)")

fig = px.bar(
    top10,
    x="Sales ($B)",
    y="Company",
    orientation="h",
    color="Sales ($B)",
    hover_name="Company"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# Sales vs Profit Scatter Plot
# -----------------------------
# Remove rows where any required scatter-plot value is missing
scatter_df = df.dropna(
    subset=[
        "Sales ($B)",
        "Profit ($B)",
        "Market Value ($B)",
        "Company",
        "Industry"
    ]
)

fig2 = px.scatter(
    scatter_df,
    x="Sales ($B)",
    y="Profit ($B)",
    size="Market Value ($B)",
    color="Industry",
    hover_name="Company"
)

st.plotly_chart(fig2, use_container_width=True)