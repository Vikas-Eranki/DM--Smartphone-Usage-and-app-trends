---
# Methodology Plan

### Smartphone Usage and App Trends Project

This document outlines the comprehensive methodology framework for the _Smartphone Usage and App Trends_ project.
It integrates research background, data preprocessing, exploratory analysis, visualization, and predictive modeling—structured across the three project phases and aligned with the team’s leadership rotation.
---

## 1. Literature Review Summary (Phase 1)

The literature review establishes a theoretical foundation for understanding app market dynamics, consumer behavior, and digital adoption trends.

• **App Popularity Determinants:**
Research emphasizes that _app ratings_, _number of installs_, and _user engagement metrics_ directly influence app visibility and long-term success (H1, H2).

• **Category-Wise Performance:**
Studies suggest certain categories (e.g., _Games, Communication, Tools_) dominate installs and engagement, indicating niche-driven market segmentation (H3).

• **Pricing & Monetization Strategies:**
Comparative analyses of _free vs. paid apps_ reveal that freemium models often outperform paid apps in installs but underperform in average rating due to in-app purchase dissatisfaction (H4).

• **User Sentiment Analysis:**
Text-mining literature highlights that _review polarity_ and _keyword frequency_ can serve as strong predictors for app retention and uninstall behavior (H5).

• **Predictive Modeling in App Markets:**
Prior works apply _Regression_ and _Classification_ models to estimate installs or ratings based on features like _reviews count, price, and content rating_ (H6).

---

## 2. Data Preprocessing Plan (Phase 1)

All preprocessing tasks will be implemented in the `data_preprocessing.ipynb` notebook to ensure clean, consistent, and analysis-ready data.

### 2.1 Handling Missing and Invalid Values

• **Rating:**
Impute missing values using median per _app category_ to preserve category-level distribution (H1).
• **Type / Price:**
Replace missing or inconsistent entries (e.g., blank price fields) using logical inferences — if Type = Free → Price = 0.
• **Content Rating:**
Standardize inconsistent text values (e.g., “Everyone 10+” vs “Everyone”).

### 2.2 Outlier & Anomaly Treatment

• **Installs:**
Remove non-numeric symbols (`+`, `,`) and convert to integer.
Detect and handle extreme outliers (> 100M installs) using percentile-based capping.
• **Reviews:**
Drop apps with _reviews > installs_, indicating erroneous entries.
• **Price:**
Remove apps with unrealistically high price values beyond the 99th percentile.

### 2.3 Feature Engineering

• **Log Transformations:**
Apply log scaling to _Reviews_ and _Installs_ for normalization.
• **Monetization Feature:**
Create a binary feature `is_paid` (1 if Price > 0, else 0).
• **Category-Level Aggregation:**
Compute average _Rating_, _Installs_, and _Reviews_ per category for comparative trend analysis.
• **Derived Metrics:**
Define `Review-to-Install Ratio` = Reviews / Installs as a proxy for engagement intensity (H2).

---

## 3. Exploratory Data Analysis (Phase 2)

_Lead:_ **Meenaksh**

The EDA phase explores relationships between app features, usage patterns, and success indicators to validate hypotheses.

| Focus Area           | Supported Hypotheses | Analytical Techniques / Expected Output                                                        |
| :------------------- | :------------------- | :--------------------------------------------------------------------------------------------- |
| Category Trends      | H3                   | Identify dominant app categories by installs and ratings; create rank-wise visual comparisons. |
| Ratings vs Installs  | H1, H2               | Correlation analysis to test if higher ratings influence install counts.                       |
| Free vs Paid Apps    | H4                   | Compare distributions of installs and ratings between monetization types.                      |
| Reviews & Engagement | H5                   | Analyze relation between review volume and average rating.                                     |
| Size & Price Impact  | H6                   | Assess how app size and price affect user satisfaction (rating).                               |

---

## 4. Visualization Plan (Phase 2 & 3)

Visual analysis helps communicate trends and correlations effectively.
Plots will be generated using **Matplotlib** and **Seaborn**, with the possibility of interactive dashboards in later phases.

| Phase   | Visualization Type                            | Purpose / Insight                                                     |
| :------ | :-------------------------------------------- | :-------------------------------------------------------------------- |
| Phase 2 | Bar Chart (Category vs Installs)              | Identify top-performing app categories (H3).                          |
| Phase 2 | Scatter Plot (Rating vs Installs)             | Examine correlation between user satisfaction and popularity (H1).    |
| Phase 2 | Box Plot (Free vs Paid – Rating Distribution) | Compare monetization impact on user ratings (H4).                     |
| Phase 2 | Histogram (App Size)                          | Understand distribution of app sizes and possible impact on installs. |
| Phase 3 | Heatmap (Feature Correlation)                 | Display multivariate relationships among features before modeling.    |
| Phase 3 | Pair Plot / Regression Plot                   | Visualize predicted vs actual installs or ratings post-modeling.      |

---

## 5. Model Training & Evaluation Plan (Phase 3)

_Lead:_ **Abhishek**

Phase 3 focuses on predictive modeling to determine the factors driving app popularity and performance.

### A. Predictive Modeling Tasks

| Prediction Task                     | Hypothesis | Model(s)                                     | Evaluation Metrics       |
| :---------------------------------- | :--------- | :------------------------------------------- | :----------------------- |
| App Popularity Prediction           | H1, H2     | Multiple Linear Regression, Random Forest    | R², RMSE                 |
| Rating Classification (High vs Low) | H4         | Logistic Regression, Decision Tree           | Accuracy, F1-Score       |
| Category Importance Analysis        | H3         | Feature Importance via Random Forest         | Feature Importance Score |
| Sentiment-Driven Success (optional) | H5         | Naïve Bayes (if text reviews are integrated) | Precision, Recall        |

---

### B. Validation & Optimization

• **Train-Test Split (80-20):**
Ensure model generalization and avoid overfitting.

• **Cross-Validation:**
Use _k-fold (k=5)_ for robust performance estimation.

• **Hyperparameter Tuning:**
Apply _GridSearchCV_ for optimizing tree-based models (e.g., max depth, n_estimators).

• **Model Interpretability:**
Use _SHAP_ and _Feature Importance plots_ to explain influential attributes on installs and ratings.

---

## 6. Deliverables by Phase Summary

| Phase       | Focus Area                    | Primary Output                                                |
| :---------- | :---------------------------- | :------------------------------------------------------------ |
| **Phase 1** | Documentation & Preprocessing | Cleaned dataset, literature and preprocessing plan            |
| **Phase 2** | EDA                           | Insights and validated hypotheses                             |
| **Phase 3** | Predictive Modeling           | Trained models, evaluation metrics, and interpretive insights |

---

## 7. Expected Outcomes

- Clear understanding of key factors influencing app success on Google Play Store
- Validated trends in category performance and monetization impact
- Predictive framework capable of estimating app popularity or rating
- Visual evidence supporting market behavior insights for mobile app developers

---
