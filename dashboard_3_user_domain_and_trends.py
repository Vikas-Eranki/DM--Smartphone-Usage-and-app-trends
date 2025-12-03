# ml_models.py
import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, accuracy_score, classification_report, confusion_matrix
import plotly.express as px
import plotly.graph_objects as go

@st.cache_data
def load_dataset():
    LOCAL="/Users/meenakshsinghania04/Desktop/DM--Smartphone-Usage-and-app-trends/Streamlit-Dashboard/dashboard_3_user_domain_and_trends.py"
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
    st.title("🤖 ML Models — Rating Prediction & Category Classification")

    df = load_dataset()
    if df is None:
        st.error("No dataset found. Place data/clean_apps.csv or configure kagglehub.")
        st.stop()

    # prepare numeric dataframe
    num = df.select_dtypes(include=[np.number]).copy()
    if num.empty:
        st.error("No numeric features available. Ensure preprocessing created numeric columns.")
        st.stop()

    task = st.selectbox("Task", ["Rating Prediction (Regression)", "Category Classification"])

    if task.startswith("Rating"):
        st.subheader("Rating Prediction (Regression)")

        if "Rating" not in num.columns:
            st.error("No 'Rating' numeric column found.")
            st.stop()

        X = num.drop(columns=["Rating"]).fillna(0)
        y = num["Rating"].fillna(num["Rating"].mean())

        test_size = st.slider("Test size (%)", 5, 50, 20)
        if st.button("Train Regression Models"):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)
            scaler = StandardScaler()
            X_train_s = scaler.fit_transform(X_train)
            X_test_s = scaler.transform(X_test)

            lr = LinearRegression()
            rf = RandomForestRegressor(n_estimators=120, random_state=42)

            lr.fit(X_train_s, y_train)
            rf.fit(X_train_s, y_train)

            lr_pred = lr.predict(X_test_s)
            rf_pred = rf.predict(X_test_s)

            st.markdown("### Linear Regression")
            st.metric("R²", f"{r2_score(y_test, lr_pred):.4f}")
            st.metric("MAE", f"{mean_absolute_error(y_test, lr_pred):.4f}")
            st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, lr_pred)):.4f}")

            st.markdown("### Random Forest")
            st.metric("R²", f"{r2_score(y_test, rf_pred):.4f}")
            st.metric("MAE", f"{mean_absolute_error(y_test, rf_pred):.4f}")
            st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, rf_pred)):.4f}")

            # plot actual vs predicted (RF)
            n = min(600, len(y_test))
            idx = np.random.choice(len(y_test), n, replace=False)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=y_test.iloc[idx], y=rf_pred[idx], mode='markers', name='Predictions'))
            fig.add_trace(go.Line(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], name='Ideal', line=dict(color='red', dash='dash')))
            fig.update_layout(xaxis_title="Actual Rating", yaxis_title="Predicted Rating")
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.subheader("Category Classification")
        if "Category" not in df.columns:
            st.error("No 'Category' column present.")
            st.stop()

        y = df["Category"]
        X = df.select_dtypes(include=[np.number]).fillna(0)
        if X.empty:
            st.error("No numeric features to train classifier.")
            st.stop()

        test_size = st.slider("Test size (%)", 5, 50, 20, key="clf_test")
        if st.button("Train Classifier"):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42, stratify=y)
            clf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
            clf.fit(X_train, y_train)
            pred = clf.predict(X_test)
            acc = accuracy_score(y_test, pred)
            st.metric("Accuracy", f"{acc*100:.2f}%")
            st.text("Classification report:")
            st.text(classification_report(y_test, pred, zero_division=0))

            cm = confusion_matrix(y_test, pred)
            fig = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual"))
            st.plotly_chart(fig, use_container_width=True)
