# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import kagglehub
# import os

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
# from sklearn.metrics import (
#     mean_squared_error, mean_absolute_error, r2_score,
#     accuracy_score, classification_report, confusion_matrix
# )

# # ------------------------------------------
# # PAGE CONFIG
# # ------------------------------------------
# st.set_page_config(
#     page_title="Google Play Store Analytics",
#     page_icon="📱",
#     layout="wide"
# )

# # ------------------------------------------
# # GLOBAL STYLES
# # ------------------------------------------
# st.markdown("""
# <style>
#     .main { background-color: #0f1116 !important; }

#     h1, h2, h3 {
#         color:white !important;
#         font-weight:600 !important;
#     }

#     .stMetric {
#         padding: 15px;
#         border-radius: 10px;
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color:white !important;
#         box-shadow: 0px 2px 6px rgba(0,0,0,0.35);
#     }

#     .block-container {
#         max-width: 1400px;
#     }

#     .sidebar .sidebar-content {
#         background-color: #111319 !important;
#     }

# </style>
# """, unsafe_allow_html=True)

# # ------------------------------------------
# # LOAD DATA
# # ------------------------------------------
# @st.cache_data
# def load_data():
#     path = kagglehub.dataset_download("vikaseranki9/google-play-store-cleaned")
#     csv_path = None
#     for f in os.listdir(path):
#         if f.endswith(".csv"):
#             csv_path = os.path.join(path, f)
#             break

#     if csv_path is None:
#         st.error("Dataset not found.")
#         st.stop()

#     df = pd.read_csv(csv_path)

#     # Auto-convert numeric fields
#     for col in ["Rating", "Reviews", "Installs"]:
#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors="coerce")

#     return df

# with st.spinner("Loading Google Play Store dataset..."):
#     df = load_data()

# # ------------------------------------------
# # SIDEBAR
# # ------------------------------------------
# st.sidebar.title(" Navigation")
# page = st.sidebar.radio(
#     "Go to:", 
#     ["Dashboard Overview", "Category Analysis", "Data Explorer"]
# )

# st.sidebar.markdown("---")
# st.sidebar.info(f"**Total Apps:** {len(df):,}")

# # ------------------------------------------
# # 🎯 PAGE 1 — DASHBOARD OVERVIEW
# # ------------------------------------------
# if page == "Dashboard Overview":

#     st.title(" Google Play Store Analytics Dashboard")
#     st.markdown("### Explore insights, categories and rating distributions.")

#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric("Total Apps", f"{len(df):,}")

#     with col2:
#         avg_rating = df["Rating"].mean()
#         st.metric("Average Rating", f"{avg_rating:.2f}")

#     with col3:
#         st.metric("Total Categories", df["Category"].nunique())

#     with col4:
#         free_pct = (df["Type"] == "Free").mean() * 100
#         st.metric("Free Apps %", f"{free_pct:.1f}%")

#     st.markdown("---")

#     c1, c2 = st.columns(2)

#     with c1:
#         st.subheader("Top 10 Categories by App Count")
#         top_cats = df["Category"].value_counts().head(10)
#         fig = px.bar(
#             x=top_cats.values,
#             y=top_cats.index,
#             orientation="h",
#             color=top_cats.values,
#             color_continuous_scale="Viridis",
#             labels={"x": "Number of Apps", "y": "Category"},
#             height=420
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with c2:
#         st.subheader("App Type Distribution")
#         types = df["Type"].value_counts()
#         fig = px.pie(
#             values=types.values,
#             names=types.index,
#             hole=0.45,
#             color_discrete_sequence=px.colors.qualitative.Set2
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     c3, c4 = st.columns(2)

#     with c3:
#         st.subheader("Rating Distribution")
#         fig = px.histogram(df, x="Rating", nbins=40, color_discrete_sequence=["#667eea"])
#         st.plotly_chart(fig, use_container_width=True)

#     with c4:
#         st.subheader("Reviews vs Rating")
#         sample = df.sample(min(1200, len(df)))
#         fig = px.scatter(
#             sample, x="Rating", y="Reviews", color="Rating",
#             color_continuous_scale="Viridis", opacity=0.65
#         )
#         st.plotly_chart(fig, use_container_width=True)

# # ------------------------------------------
# # 🎯 PAGE 2 — CATEGORY ANALYSIS
# # ------------------------------------------
# elif page == "Category Analysis":

#     st.title("📂 Category Analysis")

#     categories = ["All"] + sorted(df["Category"].unique())
#     selected = st.selectbox("Select Category", categories)

#     filtered = df if selected == "All" else df[df["Category"] == selected]

#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Apps", len(filtered))
#     col2.metric("Avg Rating", f"{filtered['Rating'].mean():.2f}")
#     col3.metric("Avg Reviews", f"{filtered['Reviews'].mean():,.0f}")
#     col4.metric("Free Apps %", f"{(filtered['Type']=='Free').mean()*100:.1f}%")

#     st.markdown("---")

#     c1, c2 = st.columns(2)

#     with c1:
#         st.subheader("Rating Distribution by Category")
#         top = df["Category"].value_counts().head(10).index
#         plot_df = df[df["Category"].isin(top)]
#         fig = px.box(plot_df, x="Category", y="Rating", color="Category")
#         fig.update_layout(height=420)
#         st.plotly_chart(fig, use_container_width=True)

#     with c2:
#         st.subheader("Average Reviews by Category")
#         avg_reviews = df.groupby("Category")["Reviews"].mean().sort_values(ascending=False).head(10)
#         fig = px.bar(
#             x=avg_reviews.values,
#             y=avg_reviews.index,
#             orientation="h",
#             color=avg_reviews.values,
#             color_continuous_scale="Blues"
#         )
#         st.plotly_chart(fig, use_container_width=True)

# # ------------------------------------------
# # 🎯 PAGE 3 — RATING ANALYSIS
# # ------------------------------------------
# elif page == "Rating Analysis":

#     st.title("⭐ Rating Analysis")

#     c1, c2 = st.columns(2)

#     with c1:
#         st.subheader("Rating Summary")
#         st.write(df["Rating"].describe())

#         st.markdown("#### Rating Ranges")
#         ranges = pd.cut(
#             df["Rating"], 
#             bins=[0, 2, 3, 4, 5],
#             labels=["Poor (0-2)", "Fair (2-3)", "Good (3-4)", "Excellent (4-5)"]
#         )
#         counts = ranges.value_counts()
#         fig = px.pie(values=counts.values, names=counts.index, color_discrete_sequence=px.colors.sequential.YlGn)
#         st.plotly_chart(fig)

#     with c2:
#         st.subheader("Rating Density")
#         fig = px.histogram(df, x="Rating", histnorm="probability density")
#         st.plotly_chart(fig)

#     st.subheader("Rating vs Reviews Correlation")
#     corr = df[["Rating", "Reviews"]].corr().iloc[0, 1]
#     st.info(f"Correlation coefficient: **{corr:.3f}**")

#     sample = df.sample(min(3000, len(df)))
#     fig = px.density_heatmap(sample, x="Rating", y="Reviews", color_continuous_scale="Viridis")
#     st.plotly_chart(fig, use_container_width=True)

# # ------------------------------------------
# # 🎯 PAGE 4 — ML MODELS
# # ------------------------------------------
# elif page == "ML Models":

#     st.title("🤖 Machine Learning Models")

#     model_type = st.selectbox("Choose Model", ["Rating Prediction", "Category Classification"])

#     # --------------------
#     # RATING PREDICTION
#     # --------------------
#     if model_type == "Rating Prediction":

#         st.subheader("Predicting App Ratings")

#         if st.button("Train Rating Models 🚀"):

#             numeric = df.select_dtypes(include=[np.number]).copy()
#             if "Rating" not in numeric.columns:
#                 st.error("No numeric Rating column available.")
#                 st.stop()

#             X = numeric.drop(columns=["Rating"]).fillna(0)
#             y = numeric["Rating"].fillna(numeric["Rating"].mean())

#             X_train, X_test, y_train, y_test = train_test_split(
#                 X, y, test_size=0.20, random_state=42
#             )

#             scaler = StandardScaler()
#             X_train = scaler.fit_transform(X_train)
#             X_test = scaler.transform(X_test)

#             lr = LinearRegression()
#             rf = RandomForestRegressor(n_estimators=160, random_state=42)

#             lr.fit(X_train, y_train)
#             rf.fit(X_train, y_train)

#             lr_pred = lr.predict(X_test)
#             rf_pred = rf.predict(X_test)

#             c1, c2 = st.columns(2)

#             with c1:
#                 st.markdown("### Linear Regression")
#                 st.metric("R²", f"{r2_score(y_test, lr_pred):.4f}")
#                 st.metric("MAE", f"{mean_absolute_error(y_test, lr_pred):.4f}")
#                 st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, lr_pred)):.4f}")

#             with c2:
#                 st.markdown("### Random Forest")
#                 st.metric("R²", f"{r2_score(y_test, rf_pred):.4f}")
#                 st.metric("MAE", f"{mean_absolute_error(y_test, rf_pred):.4f}")
#                 st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, rf_pred)):.4f}")

#             st.subheader("Prediction vs Actual (Random Forest)")
#             s = min(600, len(y_test))
#             idx = np.random.choice(len(y_test), s, replace=False)

#             fig = go.Figure()
#             fig.add_trace(go.Scatter(
#                 x=y_test.iloc[idx], y=rf_pred[idx], mode="markers",
#                 marker=dict(size=7, opacity=0.6)
#             ))
#             fig.add_trace(go.Scatter(
#                 x=[y_test.min(), y_test.max()],
#                 y=[y_test.min(), y_test.max()],
#                 mode="lines", line=dict(color="red", dash="dash")
#             ))
#             fig.update_layout(xaxis_title="Actual", yaxis_title="Predicted", height=500)
#             st.plotly_chart(fig, use_container_width=True)

#     # --------------------
#     # CATEGORY CLASSIFICATION
#     # --------------------
#     elif model_type == "Category Classification":

#         st.subheader("Classify App Category Based on Features")

#         if st.button("Train Classification Model 🚀"):

#             df_model = df.copy()
#             df_model = df_model.dropna(subset=["Category"])

#             y = df_model["Category"]
#             X = df_model.select_dtypes(include=[np.number]).fillna(0)

#             if X.empty:
#                 st.error("No numeric features available for classification.")
#                 st.stop()

#             X_train, X_test, y_train, y_test = train_test_split(
#                 X, y, test_size=0.2, random_state=42, stratify=y
#             )

#             clf = RandomForestClassifier(
#                 n_estimators=200, random_state=42, class_weight="balanced"
#             )
#             clf.fit(X_train, y_train)
#             pred = clf.predict(X_test)

#             st.markdown("### Accuracy")
#             st.metric("Accuracy", f"{accuracy_score(y_test, pred)*100:.2f}%")

#             st.markdown("### Classification Report")
#             st.text(classification_report(y_test, pred))

#             cm = confusion_matrix(y_test, pred)
#             fig = px.imshow(
#                 cm,
#                 text_auto=True,
#                 aspect="auto",
#                 labels=dict(x="Predicted", y="Actual"),
#                 color_continuous_scale="Viridis"
#             )
#             fig.update_layout(height=600)
#             st.plotly_chart(fig, use_container_width=True)

# # ------------------------------------------
# # 🎯 PAGE 5 — DATA EXPLORER
# # ------------------------------------------
# elif page == "Data Explorer":

#     st.title("📘 Data Explorer")

#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Rows", f"{len(df):,}")
#     col2.metric("Columns", len(df.columns))
#     col3.metric("Memory (MB)", f"{df.memory_usage(deep=True).sum()/1024**2:.2f}")

#     st.markdown("---")

#     if st.checkbox("Show first 10 rows", True):
#         st.dataframe(df.head(10))

#     if st.checkbox("Show statistics"):
#         st.dataframe(df.describe())

#     if st.checkbox("Show missing values"):
#         missing = df.isnull().sum()
#         missing = missing[missing > 0].sort_values(ascending=False)
#         st.dataframe(missing)

#     st.subheader("Filter by Category")
#     if "Category" in df.columns:
#         selected = st.multiselect("Category", df["Category"].unique())
#         if selected:
#             filtered = df[df["Category"].isin(selected)]
#             st.dataframe(filtered)

#             st.download_button(
#                 "Download Filtered CSV",
#                 data=filtered.to_csv(index=False),
#                 file_name="filtered.csv",
#                 mime="text/csv"
#             )

# # ------------------------------------------
# # FOOTER
# # ------------------------------------------
# st.markdown("---")
# st.markdown(
#     "<p style='text-align:center;color:#64748b;'>Google Play Store Analytics Dashboard • Streamlit © 2025</p>",
#     unsafe_allow_html=True
# )
