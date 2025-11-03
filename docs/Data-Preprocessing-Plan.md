---
# **🧮 Data Preprocessing Plan**

This document outlines the complete **data preprocessing pipeline** for the *"Smartphone Usage and App Trends"* project.
The goal is to clean, standardize, and transform the **Google Play Store dataset** into a ready-to-analyze form suitable for exploratory and predictive data mining.
---

## **1. 🎯 Objectives**

1. **Clean and validate** the raw dataset by addressing missing values, outliers, and inconsistent data formats.
2. **Standardize and normalize** numerical and categorical fields for analysis and modeling.
3. **Engineer new features** to capture patterns in app ratings, installs, and monetization types.
4. **Prepare reusable processed datasets** for:

   - Descriptive analysis
   - Predictive modeling
   - Visualization and insights

---

## **2. 📂 Source Dataset**

| Dataset File                       | Description                                           | Key Fields Used                                                                                         |
| ---------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `googleplaystore.csv`              | Core metadata and app details from Google Play Store  | `App`, `Category`, `Rating`, `Reviews`, `Size`, `Installs`, `Type`, `Price`, `Content Rating`, `Genres` |
| `googleplaystore_user_reviews.csv` | User reviews dataset for advanced text-based insights | `App`, `Translated_Review`, `Sentiment`                                                                 |

---

## **3. 🧹 Data Cleaning & Standardization**

### **3.1 Missing Values**

| Field            | Handling Strategy                                          |
| ---------------- | ---------------------------------------------------------- |
| `Rating`         | Drop nulls; ratings are key for modeling and analysis      |
| `Size`           | Replace “Varies with device” with median size per category |
| `Type`           | Fill missing with mode (“Free”)                            |
| `Price`          | Convert missing/blank to 0                                 |
| `Content Rating` | Fill with most common label (“Everyone”)                   |

---

### **3.2 Type Conversion**

- Remove non-numeric characters:

  - From `Installs` (remove `+`, `,`)
  - From `Price` (remove `$`)

- Convert:

  - `Installs`, `Reviews`, and `Price` → numeric
  - `Rating` → float

---

### **3.3 Deduplication**

- Identify duplicates by `App` + `Category`
- Keep the record with the **highest number of Reviews**

---

### **3.4 Outlier Detection and Treatment**

| Field     | Method                                 | Handling                 |
| --------- | -------------------------------------- | ------------------------ |
| `Rating`  | IQR method                             | Clip between 1.0 and 5.0 |
| `Reviews` | Log transformation                     | Reduce skewness          |
| `Price`   | Cap at 100 (exclude extreme paid apps) |                          |

---

### **3.5 Standardization**

- Convert all text fields to uppercase.
- Strip extra spaces and unify category/genre labels.
- Merge similar categories (e.g., “GAME” and “GAMES”).

---

## **4. ⚙️ Feature Engineering**

| Feature                   | Description                                          | Purpose                             |
| ------------------------- | ---------------------------------------------------- | ----------------------------------- |
| `Price_Category`          | Categorical: Free / Paid / Premium                   | Understand monetization effects     |
| `Rating_Level`            | Grouped as Low (≤3.5), Medium (3.6–4.3), High (>4.3) | Analyze satisfaction trends         |
| `Log_Installs`            | Log-transformed install counts                       | Smooth distribution for correlation |
| `Review_to_Install_Ratio` | Reviews ÷ Installs                                   | Measure engagement rate             |
| `Genre_Primary`           | Extract primary genre from multiple entries          | Simplify analysis by dominant type  |

---

## **5. 🧠 Integration & Validation**

1. Merge `googleplaystore.csv` with `googleplaystore_user_reviews.csv` on the `App` column.
2. Validate the merged dataset by:

   - Checking null counts per column
   - Ensuring column data types are consistent
   - Verifying no duplicate apps remain

3. Export final cleaned dataset as `cleaned_playstore.csv`.

---

## **6. Statistical Readiness Checks**

1. **Distribution Check:**  
   Visualize key numerical fields (`Rating`, `Installs`, `Reviews`) using histograms to understand their spread and detect skewness.

2. **Outlier Verification:**  
   Use box plots to visually confirm that outliers were handled correctly after preprocessing.

3. **Encoding:**

   - Label encode `Type` and `Content Rating`.
   - One-hot encode `Category` for modeling and visualization.

4. **Feature Scaling:**  
   Apply **Min-Max Scaling** or **StandardScaler** on numerical attributes (`Installs`, `Reviews`, `Price`) to ensure uniform range for modeling.

---

## **7. 💾 Output Artifacts**

| Artifact                    | Description                              | Format   |
| --------------------------- | ---------------------------------------- | -------- |
| `cleaned_playstore.csv`     | Final cleaned and formatted dataset      | CSV      |
| `data_summary.csv`          | Summary statistics post-cleaning         | CSV      |
| `data_preprocessing_log.md` | Record of steps, issues, and resolutions | Markdown |
| `reviews_sentiment.csv`     | Cleaned and sentiment-tagged review data | CSV      |

All processed files will be stored in the `/data/processed/` directory.

---

## **8. 🧭 Reproducibility & Automation**

- All preprocessing steps will be implemented in **Python (Pandas & NumPy)**.
- Steps will be modularized inside a notebook `data_cleaning.ipynb`.
- Logs will track missing values, dropped rows, and outlier thresholds.
- The pipeline will ensure full reproducibility and transparency for Phase 2 and 3 tasks.

---

## **9. ✅ Expected Outcomes**

- A clean, analysis-ready dataset for visualization and modeling.
- Documented and validated preprocessing pipeline.
- Reliable foundation for hypothesis testing, EDA, and predictive modeling.

---
