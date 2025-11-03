#Project Hypotheses

This document outlines the **testable hypotheses** for the *Google Play Store App Success Analysis* project, derived from the core research questions. Each hypothesis includes a corresponding null hypothesis and a proposed methodology for testing.

---

## **A. App Popularity & Marketplace Dynamics — “What Drives Success?”**

### **Research Question 1: App Category Dominance**

**Description:** Which app categories (e.g., Social, Games, Finance, Health) dominate downloads, and how has this distribution evolved over time?

* **Hypothesis (H1):** The mean number of installs (`Installs`) differs **significantly across app categories**, with “Games” and “Social” apps expected to have higher median installs compared to utility-focused categories such as “Finance” or “Education.”

  * Subpoint 1: Examine category-based install metrics.
  * Subpoint 2: Identify significant variance across categories.
* **Null Hypothesis (H0):** There is **no statistically significant difference** in the mean number of installs between app categories.
* **Methodology:**

  1. Group dataset by `Category`.
  2. Compute average and median `Installs` per category.
  3. Visualize distribution using boxplots.

---

### **Research Question 2: Impact of Monetization Strategy**

**Description:** How does the app’s monetization model (Free vs. Paid) influence ratings, installs, and user feedback?

* **Hypothesis (H1):** **Free apps** will have significantly **higher installs but lower average ratings** than paid apps.

  * Subpoint 1: Assess accessibility vs satisfaction trade-off.
  * Subpoint 2: Compare average metrics between groups.
* **Null Hypothesis (H0):** There is **no significant difference** in average ratings or install counts between free and paid apps.
* **Methodology:**

  1. Segment apps by `Type` (Free, Paid).
  2. Compare `Rating` and `Installs` using **t-tests**.
  3. Visualize differences using bar plots.
  4. Analyze correlation between price and rating.

---

### **Research Question 3: Install Predictors**

**Description:** Which combination of app metadata attributes (category, rating, reviews, size, price) best predicts high install thresholds (e.g., >1M installs)?

* **Hypothesis (H1):** A multivariate model using `Rating`, `Reviews`, and `Category` can **accurately predict** whether an app surpasses 1M installs.

  * Subpoint 1: Use classification modeling.
  * Subpoint 2: Determine predictive accuracy.
* **Null Hypothesis (H0):** Metadata features have **no predictive power** beyond random guessing.
* **Methodology:**

  1. Create binary target: `is_popular` (1 if installs > 1M).
  2. Train models (e.g., **Logistic Regression, Random Forest**).
  3. Evaluate using **AUC-ROC** and **F1-score**.
  4. Assess **feature importance**.

---

## **B. User Behavior & Perception — “Why It Works?”**

### **Research Question 4: Review Sentiment Correlation**

**Description:** Does the sentiment of user reviews correlate with app ratings and installs?

* **Hypothesis (H1):** There is a **strong positive correlation** between review sentiment polarity and app ratings.

  * Subpoint 1: Correlate sentiment with ratings.
  * Subpoint 2: Visualize sentiment vs installs.
* **Null Hypothesis (H0):** There is **no significant relationship** between sentiment polarity and either rating or installs.
* **Methodology:**

  1. Use **NLP sentiment analysis** tools (e.g., VADER, TextBlob).
  2. Aggregate sentiment scores per app.
  3. Compute correlation coefficients.
  4. Visualize via scatter plots and heatmaps.

---

### **Research Question 5: Evolution of User Concerns**

**Description:** How do recurring themes in reviews (privacy, ads, performance) evolve over time?

* **Hypothesis (H1):** Mentions of **ads** and **privacy** have increased over recent years, correlating with lower ratings.

  * Subpoint 1: Detect topic frequency trends.
  * Subpoint 2: Relate trends to user satisfaction.
* **Null Hypothesis (H0):** The frequency of these themes shows **no consistent trend** or correlation with ratings.
* **Methodology:**

  1. Apply **topic modeling (LDA)**.
  2. Track topic frequency over time.
  3. Correlate topic prevalence with mean `Rating`.
  4. Visualize using line charts.

---

## **C. Predictive Modeling & Interpretability — “How to Predict?”**

### **Research Question 6: Feature Contribution to App Success**

**Description:** Which features most influence app install counts and ratings?

* **Hypothesis (H1):** Sentiment-based and metadata features have the highest predictive contribution toward success.

  * Subpoint 1: Analyze structured + sentiment data.
  * Subpoint 2: Measure individual feature influence.
* **Null Hypothesis (H0):** All features contribute **equally or insignificantly** to model predictions.
* **Methodology:**

  1. Train models (e.g., **Random Forest Regressor, XGBoost**).
  2. Evaluate using **R²** and **RMSE**.
  3. Use **SHAP values** for interpretability.
  4. Visualize top features.

---

### **Research Question 7: Model Performance Comparison**

**Description:** Which model type provides the most accurate and interpretable predictions for app ratings?

* **Hypothesis (H1):** Tree-based ensemble models (**Random Forest**, **XGBoost**) outperform linear models.

  * Subpoint 1: Evaluate on identical datasets.
  * Subpoint 2: Compare results statistically.
* **Null Hypothesis (H0):** There is **no significant difference** in performance between model types.
* **Methodology:**

  1. Split dataset into train/test sets.
  2. Train **Ridge Regression** and **Random Forest**.
  3. Evaluate using **RMSE** and **R²**.
  4. Perform **paired t-tests** on results.

---

## **D. Regional and Temporal Trends — “How It Changes Over Time?”**

### **Research Question 8: Temporal Shifts in Category Popularity**

**Description:** How has the popularity and average rating of app categories changed over time?

* **Hypothesis (H1):** Categories like **Health & Fitness** and **Finance** have shown increased installs, while entertainment categories plateaued.

  * Subpoint 1: Examine historical growth trends.
  * Subpoint 2: Quantify temporal shifts.
* **Null Hypothesis (H0):** There are **no significant temporal changes** in installs or ratings.
* **Methodology:**

  1. Extract `Last Updated` year.
  2. Aggregate installs and ratings by category/year.
  3. Plot trends and compute regression slopes.
  4. Test slope significance using **p-values**.

---

### **Research Question 9: Regional App Adoption Patterns**

**Description:** Which regions show the highest adoption rates for different app types?

* **Hypothesis (H1):** Certain regions demonstrate **category-specific adoption patterns**.

  * Subpoint 1: Identify region-category relationships.
  * Subpoint 2: Compare install shares regionally.
* **Null Hypothesis (H0):** There are **no regional differences** in category-wise install patterns.
* **Methodology:**

  1. Use regional or proxy data.
  2. Compare install shares by category.
  3. Conduct **Chi-square tests**.
  4. Visualize using bar charts or heatmaps.

---
