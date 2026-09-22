import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Forbes_2000_Companies_2026.csv"
    )

    numeric_cols = [
        "Sales ($B)",
        "Profit ($B)",
        "Assets ($B)",
        "Market Value ($B)"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df["Country"] = (
        df["Headquarters"]
        .fillna("")
        .str.split(",")
        .str[-1]
        .str.strip()
    )

    df["Profit Margin %"] = (
        df["Profit ($B)"] /
        df["Sales ($B)"]
    ) * 100

    df["Asset Efficiency"] = (
        df["Sales ($B)"] /
        df["Assets ($B)"]
    )

    df["Market Premium"] = (
        df["Market Value ($B)"] /
        df["Assets ($B)"]
    )

    return df