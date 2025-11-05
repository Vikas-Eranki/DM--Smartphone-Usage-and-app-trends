# **Dataset Source and Description**

---

## **Dataset Source**

**Dataset:** https://www.kaggle.com/datasets/lava18/google-play-store-apps

**Description:**  
Dataset containing detailed information on Android applications listed on Google Play, including attributes such as **category, rating, reviews, size, installs, type, price, content rating, genre, last updated, current version, android version, and app name**.

---

## **Data Cleaning Process**

---

###1️ **Handling Missing and Invalid Values**

- Checked for missing values across all columns using `.isna().sum()`.  
- Dropped rows with **NaN values** in critical fields to maintain data integrity.  
- Removed entries with **invalid Rating values** (greater than 5).  
- Replaced `"Varies with device"` in **Size** column with `NaN` for consistent numeric processing.  
- Filled missing values in **Content Rating** with the **mode** of the column.  
- For **Type** column:
  - Replaced invalid values (`"0"`) with `NaN`.  
  - Standardized capitalization using `str.strip().str.capitalize()`.  
  - Dropped records with missing or invalid app type — retained only `"Free"` and `"Paid"`.

---

###2️ **Data Type Conversion**

- Converted **Reviews** to numeric using `pd.to_numeric(errors='coerce')`.  
- Cleaned and converted **Installs**:
  - Removed commas `,` and plus signs `+`.  
  - Converted to integer type.  
- Processed **Price**:
  - Removed dollar signs `$` and converted to `float`.  
- Ensured **Rating** column was numeric and within valid bounds `(1.0 ≤ Rating ≤ 5.0)`.

---

###3️ **Cleaning the Size Column**

- Implemented a helper function `convert_size()` to **standardize app size values** (e.g., KB, MB → MB).  
- Converted all size values into a uniform numeric format for better analysis.

---

###4️ **Removing Duplicates**

- Verified data consistency using `.info()` and `.duplicated()`.  
- Dropped **duplicate app entries** using the **App** column as a reference.  

---

###5️ **Outlier Handling**

- Inspected **Price, Reviews, and Installs** for unrealistic values.  
- Defined **logical thresholds** to filter out extreme outliers.  
- Ensured all numeric values lie within expected ranges.

---

###6️ **Text Standardization**

- Cleaned up extra whitespace and enforced consistent text casing across:  
  - `Category`, `App`, `Content Rating`, and `Genres`.  
- Used `.str.strip().str.title()` for uniformity and readability.

---

###7️ **Dataset Integrity Validation**

- Cross-checked logical dependencies across columns:
  - **Paid apps** must have **nonzero prices**.  
  - **Ratings** strictly between `1.0` and `5.0`.  
  - **Install counts** verified to be numeric and valid.  
- Confirmed **no null or malformed entries** remain after final cleaning.

---

###8️ **Verification**

- Used `df.info()` and `df.isna().sum()` to confirm post-cleaning validation:
  - No missing or corrupted data remain.  
  - Correct data types for all numeric and categorical features.  
  - Dataset integrity fully maintained.

---

## **Final Output**

The cleaned dataset is now ready for:

- 🔍 **Exploratory Data Analysis (EDA)**  
- 📊 **Visualization and Statistical Insights**  
- 🤖 **Machine Learning Model Preparation**

---
