# Research Methodology  
**Title: Smartphone Usage & App Trends Using Data Mining Techniques**

---

# Research Design

- The study follows a **quantitative, exploratory, descriptive, and predictive** data-mining research design to analyze smartphone app behavior using Google Play Store data.

---

## Data Source

- Dataset used: **Google Play Store Cleaned Dataset** (CSV format)  
- Total usable entries after preprocessing: **~8,500 apps**

---

## Data Collection

- Imported CSV into **Python (Pandas)**.
- Initial inspection included:
  - Data types  
  - Missing values  
  - Numeric inconsistencies  
  - Outlier checks

---

## Data Cleaning & Preprocessing

- Removed duplicate and invalid entries.
- Standardized ratings, reviews, price, size, and install fields.
- Cleaned install values by removing `"+"` and commas.
- Replaced invalid strings with `NaN` and imputed numeric values using medians.
- Dropped rows missing critical fields.
- Applied **log-transformation** to install values to reduce skewness.
- Ensured dataset is consistent and machine-learning ready.

---

# Predictive Modeling Approach

The study uses supervised machine learning to predict two outcomes:

### 1. **Install Count (Regression)**
- Uses numeric predictors such as rating, reviews, price, size, etc.

### 2. **App Popularity (Classification)**
- Defined as:  
  - `1` → installs ≥ 50,000  
  - `0` → installs < 50,000

- Features include:
  - Category  
  - Reviews  
  - Rating  
  - Price  
  - Size  
  - Last Updated Year  
  - One-hot encoded categorical values  

---

# Models Used

## Regression Model
- **Random Forest Regression** (best performer)

## Classification Models
- Logistic Regression  
- Decision Tree Classifier  
- **Random Forest Classifier** (selected model)

---

# Evaluation Metrics

### Regression:
- **RMSE**
- **MAE**
- **R² Score**

### Classification:
- **Confusion Matrix**
- **Accuracy Score**
- **Precision, Recall, F1-Score**

---

# Analytical Techniques Used

- Distribution analysis (histograms for installs & log-installs)
- Category-wise popularity trends
- Residual error analysis
- Actual vs. predicted comparison plots
- Confusion matrix heatmaps
- Feature importance evaluation

---

# Feature Engineering

- Created **log-install feature**: `installs_log = log1p(installs)`
- Created **popularity label** (`popular`)
- One-hot encoded app categories
- Scaled numeric variables using StandardScaler

---

# Visualization Strategy

- Scatter plots  
- Histograms  
- Pie charts  
- Heatmaps  
- Residual plots  
- Actual vs predicted comparison charts  

---

# Tools & Technologies

- **Python:** Pandas, NumPy  
- **Machine Learning:** Scikit-Learn  
- **Visualization:** Matplotlib, Seaborn  
- **Environment:** Google Colab  

---

# Ethical Considerations

- Dataset contains only **public metadata**, no personal data.
- No sensitive or user-specific information is involved.
- Predictions represent statistical modeling, not evaluative judgements.

---

# Outcome of the Methodology

This methodology provides a **clear, reproducible, and scalable** framework to analyze:

- Install patterns  
- App popularity  
- User engagement indicators (ratings, reviews)  
- Feature-rich vs lightweight app performance  
- Predictive markers of app success  

---

# Conclusion

This end-to-end methodology—from data extraction to supervised modeling—enables any researcher or reviewer to understand how Google Play Store data was mined and analyzed to identify factors influencing an app’s popularity and install growth.

