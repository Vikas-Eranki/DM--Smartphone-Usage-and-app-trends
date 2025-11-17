# Smartphone Usage and App Trends

**Data Mining Project – Phase 2**

---

## 1. Introduction

Smartphones have transformed how people communicate, access services, and consume content. With millions of apps available, understanding what drives app popularity provides valuable insight into user behavior and technology trends.

This project analyzes Google Play Store data to identify patterns in app performance, including the impact of categories, ratings, installs, and pricing models. Using data-mining techniques, it explores the factors that shape user engagement and app success.

---

## 2. Problem Definition for Phase 2

1. Which app categories dominate the Play Store ecosystem
2. How ratings, installs, reviews, and updates influence app success
3. Free vs Paid app behavior patterns
4. How update frequency relates to app quality and user satisfaction
5. How user behavior and smartphone characteristics shape app trends
Phase 2 focuses on discovering insights through EDA and preparing the groundwork for predictive and descriptive modeling.

---

## 3. Objectives

1. Perform comprehensive EDA with advanced and novel visualizations.
2. Generate 10–12 deep insights aligned with research questions.
3. Prepare clean, transformed, engineered datasets for modeling.
4. Begin validating hypotheses through early descriptive patterns.
5. Set up the modeling pipeline for Phase 3 (baseline + advanced models).

---

## 4. Dataset Description

**Source:** [Google Play Store Apps Dataset – Kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps)

**File:** `googleplaystore.csv`  
This dataset contains detailed information about Android apps, including category, rating, reviews, installs, type, and price.  
It supports data-mining tasks such as correlation analysis, classification, and trend discovery.

---

## 5. Methodology Overview

| Stage                           | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| **Data Cleaning & Preparation** | Missing values, duplicates, outliers, scaling, encoding       |
| **Exploratory Data Analysis**   | Category trends, rating–install relationships, pricing impact |
| **Novel Visualizations**        | Ridge plots, sunburst charts, treemaps, PCA maps, clusters    |
| **Descriptive Analysis**        | Insights mapped to research questions & hypotheses            |
| **Feature Engineering**         | New variables for modeling (Phase 3 preparation)              |


---

## 6. Team and Leadership

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

## 7. Workflow & GitHub Usage

- All tasks are organized and tracked using a shared **Notion To-Do board**, where deadlines and responsibilities are clearly assigned.
- Each member works on a **separate Git branch** named after their task (e.g., `vikas/methodology-plan`, `meenaksh/literature-review`).
- After completing a task, members **raise a Pull Request (PR)** for review and approval.
- **Commit messages** follow a structured format:  
  `Action – File or Task`  
  Example: `Added Data Preprocessing Plan – outlined missing value handling`
- Any issues or suggestions are discussed in the **PR comment section** before merging changes into the main branch.
- This workflow ensures transparent collaboration, version control, and traceable individual contributions throughout the project.

---

## 8. Repository Structure

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

## 9. Tools and Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Jupyter Notebook
- GitHub for version control
- Google Docs / Notion for collaboration

---

## 10. Phase 1 Deliverables

- Three EDA Notebooks: App / User / Smartphone domains
- Feature Engineering Document
- Updated Research Methodology (Phase 2)
- 10–12 insight summaries mapped to research questions
- Clustering and PCA notebook
- Phase 2 Insights PDF Report
- Team Contribution Log

---

## 11. Conclusion

Phase 2 shifts the project from planning to real analytical work, producing:
- High-quality EDA
- Preliminary evidence for hypotheses
- Deep domain insights
- Clean and engineered data for predictive modeling
This phase sets the foundation for Phase 3, where advanced ML models, SHAP explainability, and hypothesis testing will be executed.
