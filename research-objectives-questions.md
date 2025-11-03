# 📘 **Research Questions & Objectives**

## **1. Project Overview**

The project aims to analyze smartphone app usage and trends using large-scale datasets from sources like the Google Play Store. By applying data-mining and predictive analytics techniques, the study seeks to uncover what drives app success, user satisfaction, and adoption patterns. The focus lies on how factors such as **category, price type (free vs paid), rating, reviews, and regional differences** influence app popularity and marketplace dynamics.

**Dataset:** Google Play Store Apps — Kaggle

---

## 🎯 **Objectives**

* **Identify Key Success Drivers:**

  * Determine which app metadata factors (e.g., category, type, price, size, rating) most strongly correlate with higher install counts and user satisfaction.

* **Understand Monetization Impact:**

  * Analyze how monetization strategies (free vs paid) influence ratings, installs, and user feedback.

* **Develop Predictive Models:**

  * Build interpretable machine-learning models to predict app popularity (install count) and rating trends using app metadata and review sentiment.

* **Leverage Textual and Sentiment Features:**

  * Use natural language processing (NLP) on app reviews to identify major user concerns such as privacy, ads, and data usage — and measure their effect on ratings.

* **Visualize App Market Trends:**

  * Create interactive visualizations allowing users to explore install patterns across categories and types, highlighting the top 5 apps by downloads.

* **Ensure Transparency and Reproducibility:**

  * Follow a clear, documented data-mining pipeline with reproducible results and ethical data handling practices.

---

## ❓ **Research Questions**

### **A. App Popularity & Marketplace Dynamics — “What Drives Success?” (Metadata Focus)**

* **Category Dominance:**

  * Which app categories (e.g., Social, Games, Finance, Health) dominate downloads, and how has this distribution evolved over the years?
  * **Data needed:** Category, Installs, Last Updated

* **Monetization vs Ratings:**

  * Are free apps rated higher or lower than paid ones? How does pricing strategy affect overall satisfaction and download count?
  * **Data needed:** Type, Price, Rating, Installs

* **Install Predictors:**

  * Which combination of app attributes (category, rating, reviews, size, price) best predicts whether an app will achieve a high install threshold (e.g., >1M installs)?
  * **Data needed:** Category, Rating, Reviews, Size, Installs

---

### **B. User Behavior & Perception — “Why It Works?” (Review and Sentiment Focus)**

* **Review Sentiment Correlation:**

  * Does the sentiment of user reviews correlate with app ratings and installs, and can review tone predict user satisfaction levels?
  * **Data needed:** Reviews, Rating

* **Evolving User Concerns:**

  * How do recurring themes in reviews (privacy, ads, app performance) change over time, and what do they reveal about user expectations?
  * **Data needed:** Reviews, Last Updated, NLP-derived Topics

---

### **C. Predictive Modeling and Interpretability — “How to Predict?” (Modeling Focus)**

* **Feature Contribution to App Success:**

  * Which metadata and sentiment-based features most strongly influence app install counts and ratings?
  * **Data needed:** All structured fields + sentiment features

* **Model Performance & Interpretability:**

  * Which machine-learning models (e.g., Random Forest, XGBoost) achieve the best predictive performance for app installs and ratings, and how do interpretability methods (e.g., SHAP) explain the relative influence of each factor?
  * **Data needed:** Cleaned dataset with numeric and text-derived features

---

### **D. Regional and Temporal Trends — “How It Changes Over Time?”**

* **Regional Adoption Patterns:**

  * Which countries or regions show the fastest growth in app adoption, and are certain categories culturally favored?
  * **Data needed:** Region (if available) or proxy data, Category, Installs

* **Temporal Trends in App Categories:**

  * How have the popularity (total installs) and ratings of major app categories evolved over time, and can these trends forecast emerging user interests?
  * **Data needed:** Category, Last Updated, Installs, Rating

---

## 🧭 **Expected Outcomes**

* **Identification of key factors** that drive app downloads, engagement, and satisfaction.
* **Insights** into how pricing, category, and sentiment trends influence app success.
* **Predictive and interpretable models** for app installs and ratings.
* **An interactive dashboard** enabling dynamic exploration of app trends.
* **A reproducible, ethically sound data-mining pipeline** demonstrating robust analytics and visualization.

---

## **Scope & Limitations**

* **Scope:**

  * Focus primarily on the provided Google Play Store dataset. Supplement with external sources (App Annie, Sensor Tower, public internet statistics) only if necessary and cited. Include temporal analysis where timestamped data exists—otherwise treat time as approximate (e.g., last updated year).

* **Limitations:**

  * Kaggle dataset may be sampled, cleaned, and not capture real-time installs. Country-level install breakdowns may be missing or sparse. Causality cannot be strictly inferred from correlations observed.
