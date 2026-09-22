import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🌍 Geographic Analysis")

country = (
    df.groupby("Country")
    .agg(
        Companies=("Company","count"),
        Sales=("Sales ($B)","sum")
    )
    .reset_index()
)

fig = px.choropleth(
    country,
    locations="Country",
    locationmode="country names",
    color="Sales"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(country)