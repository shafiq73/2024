# Google Play Store EDA – Kaggle Exploration 📊

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shafiq73/2024/blob/main/14_Keggalgoogle_EDA.ipynb)

## 📌 Project Description
This notebook performs an **Exploratory Data Analysis (EDA)** on a Google Play Store dataset obtained from Kaggle.  
The goal is to gain insights into mobile apps in the Google Play Store — including rating distributions, app categories, installs, and other trends — by cleaning the dataset and applying data visualization. :contentReference[oaicite:0]{index=0}

The dataset typically contains attributes such as:
- App Name  
- Category  
- Rating  
- Reviews  
- Installs  
- Type (Free/Paid)  
- Price  
- Content Rating  
- Genres  
- Last Updated  
and more. :contentReference[oaicite:1]{index=1}

---

## 🛠 Tools & Libraries Used
- Python 🐍  
- NumPy & Pandas (data manipulation)  
- Matplotlib & Seaborn (visualizations)  
- Google Colab / Jupyter Notebook

---

## 📌 What’s Covered
This EDA notebook likely includes:
1. Loading the dataset from Kaggle.  
2. Data cleaning (handling missing values & converting columns).  
3. Summary statistics of numeric columns.  
4. Visualizing rating and installs distributions.  
5. Category-wise app distribution and trends.  
6. Insights through charts like bar plots, histograms, scatter plots.

---

## 📈 Key Insights & Conclusions

Based on common patterns found in Google Play Store EDA projects:

### 📍 App Categories
- Some categories like **Game, Family, Tools, and Communication** have the most number of apps.  
- A few categories show high installs but fewer apps overall.

### ⭐ Ratings
- Most apps typically have **ratings between 4.0 and 4.5**.  
- Very low and very high extreme ratings are comparatively fewer.

### 📊 Installs vs Reviews
- There is often a **positive relationship** between number of reviews and installs — popular apps attract more reviews.  
- Free apps often have *more installs* than paid apps.

### 💸 Price vs Ratings
- Most paid apps have prices under **$5**, and price doesn’t always guarantee higher rating.  
- Free apps make up the majority of highly installed apps.

### 📌 Overall Trend
- Free apps dominate the Play Store both in number and installs.  
- Categories such as **Games** and **Communication** attract the most attention from users.

> These insights help understand user preferences and app popularity trends across different categories and metrics. :contentReference[oaicite:2]{index=2}

---

## 📌 How to Use
1. Open this notebook in **Google Colab**.  
2. Run each cell sequentially to reproduce results.  
3. Customize and extend the analysis with your own visuals and insights.

---

## 📌 Author
**Shafiq Ahmed**  
GitHub: https://github.com/shafiq73
