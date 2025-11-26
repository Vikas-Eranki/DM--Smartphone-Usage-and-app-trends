# Smartphone Usage and App Trends

**Data Mining Project – Phase 3**

---

## 1. Introduction

Smartphones have transformed how people communicate, access services, and consume content. With millions of apps available, understanding what drives app popularity provides valuable insight into user behavior and technology trends.

This project analyzes Google Play Store data to identify patterns in app performance, including the impact of categories, ratings, installs, and pricing models. Using data-mining techniques, it explores the factors that shape user engagement and app success.

Phase 3 is the final execution phase of the project.While Phase 2 focused on EDA, insights, and model preparation, Phase 3 converts all analytical work into professional visualisations, dashboards, presentations, and final evaluation deliverables..

---

## 2. Problem Definition

- A refined narrative of findings from Phases 1 & 2
- Clear visual proof (graphs + dashboards)
- How performance issues impact long-term retention
- Model results explained with charts + interpretation
- Simple and professional communication to evaluators


---

## 3. Objectives

1. Build a high-impact PPT covering EDA, Methodology, Predictive Analysis, Findings, Conclusion.
2. Create professional static visualizations (matplotlib / seaborn).
3. Create at least 1 interactive visualization (Streamlit / Plotly).
4. Ensure clean GitHub commits, documentation uploads, and contribution logs.
5. Write the Phase 3 Final Report summarizing results and model interpretations.

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

| Stage                                   | Description                                                        |
| --------------------------------------- | ------------------------------------------------------------------ |
| **1. Visualisation Curation**           | Selecting best EDA charts + model charts, redesigning them cleanly |
| **2. Interactive Dashboards**           | Streamlit / Plotly Dash for exploring app trends                   |
| **3. Predictive Results Visualization** | Feature importance, confusion matrix, regression prediction charts |
| **4. Storyboarding PPT**                | Structuring narrative flow for presentation                        |
| **5. Final Video**                      | Clear, confident explanation of methodology + findings             |


---

## 7. Team and Leadership

| Name               | Phase Lead         | Responsibilities                                                     |
| ------------------ | ------------------ | -------------------------------------------------------------------- |
| **Vikas**          | Phase 1 Lead       | Review visuals, verify accuracy, help with model explanations        |
| **Meenaksh**       | Phase 2 Lead       | Research alignment, hypothesis linkage, PPT documentation            |
| **Abhishek Meena** | Phase 3 Lead       | Final PPT, dashboard, model visuals, presentation video coordination |


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

## 11. Phase 3 Deliverables

| Component                    | Deliverables                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------- |
| **PPT (Final Presentation)** | Full 10–12 slide deck with visuals, methods, insights, models, and conclusion |
| **Visualisations**           | 8–12 static visuals + 1 interactive dashboard                                 |
| **Video Presentation**       | 8–10 min team video, each member visible and speaking                         |
| **GitHub Contributions**     | Commit history, PPT, dashboards, reports                                      |
| **Final Report PDF**         | Phase 3 summary with visuals and interpretations                              |
| **Dashboard**                | Streamlit app showcasing installs, category trends, rating maps               |



---

## 12. Conclusion

- Interactive dashboard creation
- Strong interpretation of predictive results
- Clean GitHub collaboration
- Clear, structured, and high-quality presentation 

This phase communicates the entire project to evaluators with clarity, confidence, and visual impact.
