# Research Methodology

## **Title: Smartphone Usage & App Trends Using Data Mining Techniques**

---

## **Research Design**
This study follows a **quantitative, exploratory, descriptive, and predictive data-mining methodology** to examine smartphone app behavior using Google Play Store data.  
The goal is to understand how app characteristics and feature-richness influence **user satisfaction, popularity, and install trends** across categories.

---

## **Data Source**
**Dataset Used:** Google Play Store Cleaned Dataset  
**Format:** CSV  
**Total usable entries after preprocessing:** ~8,500+ apps

### **Key Attributes Used**
- Category  
- Rating  
- Reviews  
- Size (MB) / File size (if available)  
- Price  
- Installs (cleaned & transformed)  
- Last Updated (Year extracted)  
- Primary Genre  

---

## **Data Collection**
- Dataset imported using **Python (Pandas)**
- Initial inspection performed on:
  - Data types  
  - Missing values  
  - Numeric inconsistencies  
  - Outlier ranges  
- Columns standardized (lowercase, underscores) for ML modeling

---

## **Data Cleaning & Preprocessing**
Steps performed to ensure high-quality data:

### **1. Duplicate Removal**
Removed all repeated records to maintain unique app entries.

### **2. Handling Missing Values**
- Converted invalid strings to `NaN`
- Dropped rows missing critical fields like rating or installs
- Filled minor numeric NaNs using **median**

### **3. Standardization & Type Conversion**
- Cleaned install values (removed commas and “+” signs)
- Converted reviews, price, and rating to numeric
- Fixed extreme values (e.g., invalid ratings > 5)

### **4. Outlier Filtering**
- Removed apps with unrealistic install/rating values
- Applied **log-transformation** to fix install count skewness

**Outcome:** Clean, consistent, machine-learning-ready dataset.

---

## **Feature Engineering**

### **1. Log Install Feature (Regression Target)**
installs_log = log1p(installs)
Used because installs are extremely skewed (10 → 1,000,000,000).

### **2. Popularity Label (Classification Target)**
popular = 1 if installs >= 50,000
popular = 0 otherwise
Binary classification: **popular vs. not-popular**.

### **3. One-Hot Encoding**
- Category encoded into binary columns  
- Ensures models do not misinterpret categories as numeric order

### **4. Scaling**
- Applied **StandardScaler** on numeric features for regression balance

---

## **Predictive Modeling Approach**
A supervised learning approach consisting of:

### ✔ **Regression Model**
Predicts install counts using:
- Category  
- Reviews  
- Rating  
- Price  
- Size (if available)

### ✔ **Classification Model**
Predicts whether an app is likely to be **popular**.

Together, these models examine how features and category attributes impact app adoption.

---

## **Models Used**

### **Regression Models**
- Linear Regression  
- **Random Forest Regression (best performer)**

### **Classification Model**
- **Random Forest Classifier**

---

## **Evaluation Metrics**

### **Regression Metrics**
- **RMSE** – measures large errors  
- **MAE** – interpretable average error  
- **R² Score** – variance explained  

### **Classification Metrics**
- Accuracy Score  
- Classification Report (Precision, Recall, F1)  
- Confusion Matrix (false positives & negatives)

These metrics provide transparent, measurable model performance.

---

## **Analytical Techniques Used**
- Distribution analysis (histograms for installs & log-installs)
- Category-wise popularity analysis
- Scatter plots (actual vs predicted installs)
- Residual analysis
- Pie charts (popular vs non-popular)
- Error comparison (baseline vs trained model)

---

## **Visualization Strategy**
Used the following visual tools:
- Scatter plots  
- Histograms  
- Pie charts  
- Confusion matrix heatmaps  
- Predicted vs. actual comparison  
- Residual plots  

---

## **Tools & Technologies**
- **Python:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Machine Learning:** Scikit-Learn  
- **Environment:** Google Colab  

---

## **Ethical Considerations**
- Dataset contains public metadata only  
- No personal user information (PII) involved  
- Predictions are statistical, not evaluative of individuals or developers  

---

## **Outcome of the Methodology**
This methodology provides a complete, reproducible framework to:

- Understand patterns in app installs & popularity  
- Analyze impact of user engagement (reviews, ratings)  
- Compare feature-rich vs. lightweight apps  
- Predict install counts with high accuracy  
- Classify app popularity  
- Provide insights for developers & market analysts  

### **Key Findings**
➡ **User engagement signals (reviews, ratings)** influence installs more than app size.  
➡ Random Forest Regression achieved **R² ≈ 0.91**, indicating strong predictive power.  
➡ Popularity classification is moderately accurate and will improve in Phase 3.

---

##  **Conclusion**
This research methodology ensures a fully structured process—from dataset preprocessing to predictive modeling—allowing any reviewer or researcher to clearly understand how Google Play Store data was mined, analyzed, and interpreted to answer the research question.
