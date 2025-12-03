# category_analysis.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import numpy as np

@st.cache_data
def load_dataset():
    LOCAL = "/Users/meenakshsinghania04/Desktop/DM--Smartphone-Usage-and-app-trends/data/processed/googleplaystore_cleaned.csv"
    if os.path.exists(LOCAL):
        return pd.read_csv(LOCAL)
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
    st.title(" Category Analysis")

    df = load_dataset()
    if df is None:
        st.error("No dataset found. Place data/clean_apps.csv or configure kagglehub.")
        st.stop()

    # ensure numeric conversion
    for c in ["Installs","Reviews","Rating","Price","Size"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    cats = ["All"] + sorted(df["Category"].dropna().unique().tolist()) if "Category" in df.columns else ["All"]
    sel = st.selectbox("Select Category", cats)

    filtered = df if sel == "All" else df[df["Category"] == sel]

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Apps", f"{len(filtered):,}")
    c2.metric("Avg Rating", f"{filtered['Rating'].mean():.2f}" if "Rating" in filtered.columns else "N/A")
    c3.metric("Avg Reviews", f"{filtered['Reviews'].mean():.0f}" if "Reviews" in filtered.columns else "N/A")
    c4.metric("Free %", f"{(filtered['Type']=='Free').mean()*100:.1f}%" if "Type" in filtered.columns else "N/A")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("Rating Distribution (Top Categories)")
        if "Category" in df.columns and "Rating" in df.columns:
            top = df["Category"].value_counts().head(12).index.tolist()
            plot_df = df[df["Category"].isin(top)]
            fig = px.box(plot_df, x="Category", y="Rating", title="Rating by Category")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need 'Category' and 'Rating' columns")

    with right:
        st.subheader("Average Reviews by Category (Top 15)")
        if "Category" in df.columns and "Reviews" in df.columns:
            avg_rev = df.groupby("Category")["Reviews"].mean().sort_values(ascending=False).head(15)
            fig = px.bar(x=avg_rev.values, y=avg_rev.index, orientation="h", labels={"x":"Avg Reviews","y":"Category"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need 'Category' and 'Reviews' columns")

    st.markdown("---")
    st.subheader("Free vs Paid — Comparison")
    if set(["Type","Rating","Installs"]) & set(df.columns):
        metric = st.selectbox("Metric to compare", options=[c for c in ["Rating","Installs","Reviews"] if c in df.columns], index=0, key="cat_metric")
        fig = px.box(df.dropna(subset=[metric,"Type"]), x="Type", y=metric, points="outliers", title=f"{metric} by Type (Free vs Paid)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Need 'Type' plus numeric metric columns")
