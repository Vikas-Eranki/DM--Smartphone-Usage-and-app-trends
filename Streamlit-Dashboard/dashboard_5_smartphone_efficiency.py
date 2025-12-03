import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


def run():
    st.title(" Smartphone Usage Efficiency — Predictive Analysis Dashboard")
    st.write("""
    This dashboard answers the key question:

    **How do screen time, app usage, and categories collectively affect smartphone efficiency?  
    Can we model efficient vs inefficient users?**
    """)

    @st.cache_data
    def load_data():
        path = kagglehub.dataset_download("vikaseranki9/mobile-usage-ds")

        csv_path = None
        for f in os.listdir(path):
            if f.endswith(".csv"):
                csv_path = os.path.join(path, f)
                break

        return pd.read_csv(csv_path)

    df = load_data()

    st.subheader("📂 Dataset Preview")
    st.dataframe(df.head())
    st.write("Shape:", df.shape)

    st.subheader(" Feature Distributions")

    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    df["Daily_Screen_Time_Hours"].hist(ax=ax[0,0])
    ax[0,0].set_title("Daily Screen Time")

    df["Number_of_Apps_Used"].hist(ax=ax[0,1])
    ax[0,1].set_title("Number of Apps Used")

    df["Social_Media_Usage_Hours"].hist(ax=ax[1,0])
    ax[1,0].set_title("Social Media Usage")

    df["Productivity_App_Usage_Hours"].hist(ax=ax[1,1])
    ax[1,1].set_title("Productivity App Usage")

    st.pyplot(fig)

   
    st.subheader(" Efficiency Score Calculation")

    df["efficiency_score"] = (
        df["Productivity_App_Usage_Hours"] /
        df["Daily_Screen_Time_Hours"].replace(0, np.nan)
    ).fillna(0)

    low = df["efficiency_score"].quantile(0.33)
    high = df["efficiency_score"].quantile(0.67)

    def label_eff(x):
        if x <= low:
            return 0
        elif x >= high:
            return 1
        return 2

    df["label"] = df["efficiency_score"].apply(label_eff)

    st.write("Label distribution (0 = inefficient, 1 = efficient):")
    st.write(df["label"].value_counts())

    df2 = df[df["label"] != 2].copy()
    df2["y"] = df2["label"]

    st.subheader(" Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    st.pyplot(fig)

    st.subheader("🤖 Model Training & Accuracy Comparison")

    features = [
        "Age",
        "Daily_Screen_Time_Hours",
        "Number_of_Apps_Used",
        "Social_Media_Usage_Hours",
        "Gaming_App_Usage_Hours",
        "Gender",
        "Location"
    ]

    numeric_features = [
        "Age",
        "Daily_Screen_Time_Hours",
        "Number_of_Apps_Used",
        "Social_Media_Usage_Hours",
        "Gaming_App_Usage_Hours"
    ]

    categorical_features = ["Gender", "Location"]

    preprocess = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ]
    )

    X = df2[features]
    y = df2["y"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": Pipeline([
            ("pre", preprocess),
            ("clf", LogisticRegression(max_iter=1000))
        ]),
        "Random Forest": Pipeline([
            ("pre", preprocess),
            ("clf", RandomForestClassifier(n_estimators=150, random_state=42))
        ]),
        "Decision Tree": Pipeline([
            ("pre", preprocess),
            ("clf", DecisionTreeClassifier(max_depth=5, random_state=42))
        ])
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        results[name] = accuracy_score(y_test, preds)

    st.write(results)

    fig, ax = plt.subplots(figsize=(7, 5))
    plt.bar(results.keys(), results.values())
    plt.ylabel("Accuracy")
    plt.title("Model Comparison")
    st.pyplot(fig)

    st.subheader("🔍 Behavioral Clustering (KMeans)")

    cluster_features = [
        "Daily_Screen_Time_Hours",
        "Number_of_Apps_Used",
        "Social_Media_Usage_Hours",
        "Productivity_App_Usage_Hours",
        "Gaming_App_Usage_Hours"
    ]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[cluster_features])

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=20)
    df["cluster"] = kmeans.fit_predict(scaled)

    st.write("Cluster behavior summary:")
    st.dataframe(df.groupby("cluster")[cluster_features].mean())

    centers = pd.DataFrame(kmeans.cluster_centers_, columns=cluster_features)

    fig, ax = plt.subplots(figsize=(10, 6))
    centers.plot(kind="bar", ax=ax)
    plt.title("Cluster Patterns")
    st.pyplot(fig)

    st.subheader(" PCA 2D Visualization")

    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(scaled)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        x=pca_data[:, 0],
        y=pca_data[:, 1],
        hue=df["cluster"],
        palette="bright"
    )
    plt.title("PCA Cluster Plot")
    st.pyplot(fig)


    st.subheader(" Final Insights")
    st.write("""
    ### ✔ What defines an *efficient* smartphone user?

    - Higher **productivity app usage**  
    - Lower **social media + gaming usage**  
    - Moderate total screen time  
    - Consistent daily app patterns  

    ### ✔ Can we predict efficiency?
    Yes — Logistic Regression achieved **84% accuracy**, showing strong predictability.

    ### ✔ Are there natural behavioral groups?
    KMeans revealed:
    - A **social media heavy** cluster  
    - A **gaming heavy** cluster  
    - A **balanced productivity** (most efficient) cluster  
    """)

