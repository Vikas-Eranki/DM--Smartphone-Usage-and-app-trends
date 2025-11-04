---
#  **Data Preprocessing Plan – Smartphone Usage & App Trends**

This document outlines the complete data preprocessing pipeline for analyzing the **Google Play Store dataset** as part of the *Smartphone Usage and App Trends* project.
---

## **1. Objective**

Prepare a clean, structured, and analysis-ready dataset to:

- Understand app success factors (downloads, ratings, reviews, monetization).
- Analyze category-wise trends and user engagement patterns.
- Enable descriptive and predictive modeling.
- Support interactive visualizations (Top 5 apps by category and type).

---

## **2. Data Sources**

| Dataset                            | Description                                                            |
| ---------------------------------- | ---------------------------------------------------------------------- |
| `googleplaystore.csv`              | App metadata (category, rating, installs, price, content rating, etc.) |
| `googleplaystore_user_reviews.csv` | User reviews with sentiments (Positive/Negative/Neutral)               |

---

## **3. Data Cleaning**

### **3.1 Remove Duplicates**

- Identify duplicates using `App + Category`
- Keep the entry with the highest number of `Reviews`

### **3.2 Handle Missing Values**

| Column           | Strategy                                                                     |
| ---------------- | ---------------------------------------------------------------------------- |
| `Rating`         | Drop rows where `Rating` is NaN                                              |
| `Type`           | Replace missing or `"0"` with mode (`Free`)                                  |
| `Content Rating` | Fill with mode                                                               |
| `Size`           | Replace `"Varies with device"` with NaN → later fill with median by category |
| Other Columns    | If still NaN in non-essential fields → drop those rows                       |

### **3.3 Convert Data Types**

| Column         | Conversion                                                 |
| -------------- | ---------------------------------------------------------- |
| `Reviews`      | Convert to numeric (int)                                   |
| `Installs`     | Remove `+`, `,` → convert to integer                       |
| `Price`        | Remove `$` → convert to float                              |
| `Size`         | Convert `M` to bytes (×1,000,000), `k/K` to bytes (×1,000) |
| `Last Updated` | Convert to datetime                                        |
| `Genres`       | Extract primary genre before `;`                           |

---

## **4. Outlier Detection & Treatment**

| Feature              | Method                                                              | Handling |
| -------------------- | ------------------------------------------------------------------- | -------- |
| `Rating`             | Values > 5 removed                                                  |          |
| `Price`              | Cap at $100 to remove extreme values                                |          |
| `Reviews & Installs` | Apply log transformation (`log1p()`) during analysis (not cleaning) |          |
| `Size`               | Winsorize extreme values if necessary                               |          |

---

## **5. Feature Engineering**

| New Feature               | Description                               |
| ------------------------- | ----------------------------------------- |
| `Price_Type`              | Free / Paid / Premium (`Price > 5`)       |
| `Rating_Level`            | Low (≤3.5), Medium (3.6–4.3), High (>4.3) |
| `Log_Installs`            | `log(Installs + 1)`                       |
| `Review_to_Install_Ratio` | Reviews ÷ Installs                        |
| `Days_Since_Last_Update`  | `(Today - Last Updated)`                  |
| `Genre_Primary`           | First genre from `Genres` column          |
| `Sentiment_Polarity`      | From user reviews dataset                 |

---

## **6. Merge Datasets**

- If using the user reviews dataset, first summarize the sentiment (positive, negative, neutral) for each app.
- Then merge this summarized review data with the main app dataset using the app name as the common key.
- This adds user opinion insights alongside installs, ratings, and other app attributes.

---

## **7. Data Validation & Final Checks**

| Check        | Action                                         |
| ------------ | ---------------------------------------------- |
| Null values  | Ensure 0 nulls remain in critical fields       |
| Data types   | Confirm numeric/categorical fields are correct |
| Unique apps  | Verify duplicates removed                      |
| Value ranges | Rating (1–5), Price ≥ 0, Installs ≥ 0          |
| Save output  | Export as `cleaned_playstore.csv`              |

---

## **8. Output Files**

| File Name               | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `cleaned_playstore.csv` | Final processed dataset                                   |
| `data_summary.csv`      | Summary statistics                                        |
| `preprocessing_log.md`  | Document of changes, dropped rows, missing values handled |
| `reviews_sentiment.csv` | Processed user reviews dataset                            |

---

## **9. Tools & Libraries**

- **Python:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Visualization:** Plotly/Dash/Streamlit (for interactive plot)
- **Notebook:** `data_preprocessing.ipynb`

---

## **10. Expected Outcomes**

- **Clean and reliable dataset** prepared after preprocessing, ready for Exploratory Data Analysis (EDA) and modeling.
- **Feature-rich data** enabling development of accurate and robust predictive models.
- **Actionable insights** into factors influencing app success such as downloads, ratings, and user sentiment.
- **Interactive visualizations** showcasing category-wise installs and comparisons between Free vs. Paid apps.

---
