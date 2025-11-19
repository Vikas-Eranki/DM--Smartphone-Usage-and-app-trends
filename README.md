# Smartphone Usage and App Trends

**Data Mining Project – Phase 2**

---

## 1. Introduction

Smartphones have transformed how people communicate, access services, and consume content. With millions of apps available, understanding what drives app popularity provides valuable insight into user behavior and technology trends.

This project analyzes Google Play Store data to identify patterns in app performance, including the impact of categories, ratings, installs, and pricing models. Using data-mining techniques, it explores the factors that shape user engagement and app success.

Phase 2 performs an exemplary Exploratory Data Analysis (EDA) to uncover patterns related to app updates, user expectations, performance, security concerns, and category dynamics. Insights obtained here form the analytical foundation for the predictive and descriptive models in Phase 3.

---

## 2. Problem Definition

- Whether frequent updates maintain relevance and trust
- How reviews, ratings, and installs evolve with user expectations
- How performance issues impact long-term retention
- How feature-rich vs lightweight apps differ in satisfaction
- Why security concerns, especially in finance apps, lead to drop-offs
- How apps compete across categories over time

---

## 3. Objectives

1. Perform comprehensive EDA with advanced and novel visualizations.
2. Generate 10–12 deep insights aligned with research questions.
3. Prepare clean, transformed, engineered datasets for modeling.
4. Begin validating hypotheses through early descriptive patterns.
5. Set up the modeling pipeline for Phase 3 (baseline + advanced models).
6. Clustering, dimensionality reduction, and preparatory modeling steps

---

## 4. Dataset Description

**Source:** [Google Play Store Apps Dataset – Kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps)

**File:** `googleplaystore.csv`  
This dataset contains detailed information about Android apps, including category, rating, reviews, installs, type, and price.  
It supports data-mining tasks such as correlation analysis, classification, and trend discovery.

---

## 5. Exploratory Research Analysis for EDA

1) How do frequent updates, the number of new reviews, and changing rankings in top categories help us understand what users expect and how top apps compete over time.
2) How do feature-rich apps (large size, multiple permissions, many functionalities) compare to lightweight apps in terms of user satisfaction, update frequency, and long-term retention across different categories?

---

## 6. Methodology Overview

| Stage                           | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| **Data Cleaning & Preparation** | Missing values, duplicates, outliers, scaling, encoding       |
| **Exploratory Data Analysis**   | Category trends, rating–install relationships, pricing impact |
| **Novel Visualizations**        | Ridge plots, sunburst charts, treemaps, PCA maps, clusters    |
| **Descriptive Analysis**        | Insights mapped to research questions & hypotheses            |
| **Feature Engineering**         | New variables for modeling (Phase 3 preparation)              |


---

## 7. Team and Leadership

| Name         | Lead         | Primary Focus                                              |
| ------------ | ------------ | ---------------------------------------------------------- |
| **Vikas**    | Phase 1 Lead | Methodology, preprocessing plan, documentation integration |
| **Meenaksh** | Phase 2 Lead | Research objectives, hypotheses, literature review         |
| **Abhishek** | Phase 3 Lead | Dataset rationale, data description, final review          |

**Leadership Rotation:**

- Phase 1 – Vikas
- Phase 2 – Meenaksh
- Phase 3 – Abhishek

This rotation ensures balanced involvement across all technical and analytical stages.
Detailed phase-wise task allocations and individual responsibilities are documented separately in the work_division_plan.docx file.

---

## 8. Workflow & GitHub Usage

- All tasks are organized and tracked using a shared **Notion To-Do board**, where deadlines and responsibilities are clearly assigned.
- Each member works on a **separate Git branch** named after their task (e.g., `vikas/methodology-plan`, `meenaksh/literature-review`).
- After completing a task, members **raise a Pull Request (PR)** for review and approval.
- **Commit messages** follow a structured format:  
  `Action – File or Task`  
  Example: `Added Data Preprocessing Plan – outlined missing value handling`
- Any issues or suggestions are discussed in the **PR comment section** before merging changes into the main branch.
- This workflow ensures transparent collaboration, version control, and traceable individual contributions throughout the project.

---

## 9. Repository Structure

```
smartphone-app-trends/
│
├── data/
│   ├── raw/googleplaystore.csv
│   └── processed/cleaned_data_phase2.csv
│
├── docs/
│   ├── literature_review_summary.docx
│   ├── research_objectives.docx
│   ├── hypotheses_and_innovation.docx
│   ├── methodology_plan.docx
│   ├── feature_engineering_strategy.docx
│   └── phase2_methodology_updated.docx
│
├── notebooks/
│   ├── eda_app_domain_vikas.ipynb
│   ├── eda_user_domain_meenaksh.ipynb
│   ├── eda_smartphone_domain_abhishek.ipynb
│   ├── clustering_and_pca.ipynb
│   └── shap_preparation.ipynb
│
├── reports/
│   ├── phase1_report_compiled.pdf
│   └── phase2_insights_report.pdf
│
└── README.md
```

---

## 10. Tools and Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn
- Jupyter Notebook
- GitHub for version control
- Google Docs / Notion for collaboration

---

## 11. Phase 2 Deliverables

| Category                              | Deliverables                                                                                                                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Exploratory Data Analysis (EDA)**   | • EDA notebooks based on research questions and hypothesis<br>• Visualizations including novel charts (treemap, PCA, clusters)<br>• Cleaned & transformed dataset for analysis<br>• Insight summary (10–12 insights) aligned with the 3 final research questions                |
| **Research Methodology**              | • Updated Phase-2 methodology document (approach, justification, techniques)<br>• Feature engineering strategy (variables for modeling)<br>• Preliminary linkage of EDA findings to research questions and hypotheses                                                                             |
| **Predictive & Descriptive Analysis** | • Baseline modeling preparation notebooks (variable checks, preprocessing outputs)<br>• PCA & clustering analysis for descriptive insights<br>• Pre-modeling plots: correlations, feature distributions, clusters<br>• Model-readiness datasets and preprocessing pipeline (for Phase 3 modeling) |


---

## 12. Conclusion

- High-quality EDA
- Preliminary evidence for hypotheses
- Deep domain insights using visualizations
- Clean and engineered data for predictive modeling  
This phase sets the foundation for Phase 3, where advanced ML models, SHAP explainability, and hypothesis testing will be executed.
