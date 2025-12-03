# overview.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# -------------------------
# Data loader helper (shared)
# -------------------------
@st.cache_data
def load_dataset():
    # prefer local cleaned CSV
    LOCAL = "/Users/meenakshsinghania04/Desktop/DM--Smartphone-Usage-and-app-trends/data/processed/googleplaystore_cleaned.csv"
    if os.path.exists(LOCAL):
        df = pd.read_csv(LOCAL)
        return df
    # fallback: try kagglehub (if installed & configured)
    try:
        import kagglehub
        path = kagglehub.dataset_download("vikaseranki9/google-play-store-cleaned")
        for f in os.listdir(path):
            if f.endswith(".csv"):
                return pd.read_csv(os.path.join(path, f))
    except Exception:
        pass
    return None

def run():
    st.title(" Overview / Snapshot")

    df = load_dataset()
    if df is None:
        st.error("No dataset found. Put cleaned CSV at data/clean_apps.csv or install/configure kagglehub.")
        st.stop()

    # Quick cleanup and ensure numeric
    for c in ["Installs", "Reviews", "Rating", "Price", "Size"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Apps", f"{df['App'].nunique():,}" if "App" in df.columns else f"{len(df):,}")
    col2.metric("Total Installs", f"{int(df['Installs'].sum()):,}" if "Installs" in df.columns else "N/A")
    col3.metric("Average Rating", f"{df['Rating'].mean():.2f}" if "Rating" in df.columns else "N/A")
    col4.metric("Categories", f"{df['Category'].nunique():,}" if "Category" in df.columns else "N/A")

    st.markdown("---")

    st.subheader("Top Apps by Metric")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    metric = st.selectbox("Metric", options=["Installs", "Reviews", "Rating"] if set(["Installs","Reviews","Rating"]) & set(df.columns) else numeric_cols)
    K = st.slider("Top K", 5, 100, 10)
    order = st.radio("Sort order", ["Descending","Ascending"]) == "Descending"
    topk = df.sort_values(by=metric, ascending=not order).head(K)
    st.dataframe(topk[["App","Category", metric]].fillna("N/A").reset_index(drop=True))

    st.markdown("---")
    left, right = st.columns(2)

    with left:
        st.subheader("Install distribution")
        if "Installs" in df.columns:
            bins = st.slider("Bins", 20, 200, 60, key="bins_overview")
            fig = px.histogram(df, x="Installs", nbins=bins, title="Installs distribution (may be skewed)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No 'Installs' column")

    with right:
        st.subheader("Reviews vs Rating")
        if set(["Reviews","Rating"]) <= set(df.columns):
            sample = df.sample(min(2000, len(df)))
            fig = px.scatter(sample, x="Rating", y="Reviews", color="Category" if "Category" in df.columns else None,
                             hover_name="App" if "App" in df.columns else None, opacity=0.6)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need 'Rating' and 'Reviews' columns")
