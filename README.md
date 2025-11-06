# Smartphone Usage and App Trends

**Data Mining Project – Phase 1**

---

## 1. Introduction

Smartphones have transformed how people communicate, access services, and consume content. With millions of apps available, understanding what drives app popularity provides valuable insight into user behavior and technology trends.

This project analyzes Google Play Store data to identify patterns in app performance, including the impact of categories, ratings, installs, and pricing models. Using data-mining techniques, it explores the factors that shape user engagement and app success.

---

## 2. Problem Definition

The study examines how various attributes influence app success on the Play Store. It focuses on:

- Dominant app categories and their growth trends
- Correlation between app ratings and installs
- Differences between free and paid apps in satisfaction and engagement
- Common user concerns and expectations seen in reviews

---

## 3. Objectives

1. Identify leading app categories and usage trends.
2. Examine relationships between ratings, installs, and monetization types.
3. Assess how pricing strategy affects popularity.
4. Plan data cleaning and exploratory analysis steps.
5. Define the methodology for descriptive and predictive modeling.

---

## 4. Dataset Description

**Source:** [Google Play Store Apps Dataset – Kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps)

**File:** `googleplaystore.csv`  
This dataset contains detailed information about Android apps, including category, rating, reviews, installs, type, and price.  
It supports data-mining tasks such as correlation analysis, classification, and trend discovery.

---

## 5. Methodology Overview

The project follows three phases:

| Phase | Focus                          | Description                                                             |
| ----- | ------------------------------ | ----------------------------------------------------------------------- |
| **1** | Planning & Documentation       | Problem definition, dataset study, hypotheses, and methodology planning |
| **2** | Data Exploration               | Data cleaning, exploratory analysis.                                    |
| **3** | Predictive Modeling & Insights | Building and evaluating models, generating insights                     |

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
│   ├── raw/
│   │   └── googleplaystore.csv
│   └── processed/
│       └── cleaned_sample.csv
│
├── docs/
│   ├── work_division_plan.docx
│   ├── research_objectives.docx
│   ├── hypotheses_and_innovation.docx
│   ├── dataset_description_and_rationale.docx
│   ├── literature_review_summary.docx
│   ├── data_preprocessing_plan.docx
│   └── methodology_plan.docx
│
├── notebooks/
│   └── data_exploration.ipynb
│
├── reports/
│   └── phase1_report_compiled.pdf
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

- README.md
- Work Division Plan
- Research Objectives
- Hypotheses and Innovation
- Dataset Description and Rationale
- Literature Review Summary
- Data Preprocessing Plan
- Methodology Plan
- Compiled Phase 1 Report (PDF)

---

## 11. Conclusion

Phase 1 defines the problem, sets objectives, and establishes a clear understanding of the dataset.  
The structured plan developed here will guide subsequent phases of exploration, analysis, and modeling to uncover meaningful insights into app usage and trends.
