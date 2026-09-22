import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("💰 Financial Performance")

metric = st.selectbox(
    "Metric",
    [
        "Profit Margin %",
        "Asset Efficiency",
        "Market Premium"
    ]
)

top = df.nlargest(20, metric)

fig = px.bar(
    top,
    x="Company",
    y=metric,
    color=metric
)

st.plotly_chart(fig, use_container_width=True)

corr = df[
    [
        "Sales ($B)",
        "Profit ($B)",
        "Assets ($B)",
        "Market Value ($B)"
    ]
].corr()

st.dataframe(corr)