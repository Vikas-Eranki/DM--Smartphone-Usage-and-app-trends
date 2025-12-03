# data_explorer.py
import streamlit as st
import pandas as pd
import os
import numpy as np

@st.cache_data
def load_dataset():
    LOCAL="/Users/meenakshsinghania04/Desktop/DM--Smartphone-Usage-and-app-trends/Streamlit-Dashboard/dashboard_4_overall_modeling_overview.py"
    if os.path.exists(LOCAL):
        return pd.read_csv(LOCAL)
    try:
        import kagglehub
        path=kagglehub.dataset_download("vikaseranki9/google-play-store-cleaned")
        for f in os.listdir(path):
            if f.endswith(".csv"):
                return pd.read_csv(os.path.join(path, f))
    except Exception:
        pass
    return None

def run():
    st.title("📘 Data Explorer")

    df = load_dataset()
    if df is None:
        st.error("No dataset found. Put data/clean_apps.csv or configure kagglehub.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", f"{len(df):,}")
    col2.metric("Columns", f"{len(df.columns)}")
    mem = df.memory_usage(deep=True).sum()/1024**2
    col3.metric("Memory (MB)", f"{mem:.2f}")

    st.markdown("---")
    if st.checkbox("Show head (10)", True):
        st.dataframe(df.head(10))

    if st.checkbox("Show descriptive stats"):
        st.dataframe(df.describe(include='all').T)

    if st.checkbox("Show missing values"):
        miss = df.isnull().sum()
        miss = miss[miss>0].sort_values(ascending=False)
        st.dataframe(miss)

    st.markdown("---")
    st.subheader("Filter & Download")
    if "Category" in df.columns:
        cats = st.multiselect("Category", df["Category"].unique().tolist())
        out = df[df["Category"].isin(cats)] if cats else df
    else:
        out = df

    st.dataframe(out.head(200))
    st.download_button("Download CSV (filtered)", data=out.to_csv(index=False), file_name="filtered_apps.csv")
