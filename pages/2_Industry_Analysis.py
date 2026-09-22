import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🏭 Industry Analysis")

summary = (
    df.groupby("Industry")
    .agg(
        Companies=("Company","count"),
        Sales=("Sales ($B)","sum"),
        Profit=("Profit ($B)","sum"),
        Assets=("Assets ($B)","sum")
    )
    .reset_index()
)

st.dataframe(summary)

fig = px.treemap(
    summary,
    path=["Industry"],
    values="Sales"
)

st.plotly_chart(fig, use_container_width=True)