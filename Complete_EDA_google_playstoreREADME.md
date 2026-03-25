GitHub Project Structure: Google Play Store EDA
Google_Playstore_EDA/
│
├─ 05_complete_EDA_google_playstore_data.ipynb
├─ README.md
├─ data/
│   └─ google_playstore_data.csv      # Place your dataset here
└─ images/
    └─ example_plot.png               # Optional saved plots from notebook
README.md (Portfolio-ready with badges & conclusions)
# Google Play Store EDA 📊

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shafiq73/2024/blob/main/05_complete_EDA_google_playstore_data.ipynb)

## Project Description
This project performs a **complete Exploratory Data Analysis (EDA)** on the Google Play Store dataset to understand app trends, ratings, categories, reviews, and installs.  

**Dataset:** CSV containing app name, category, rating, reviews, installs, type, price, and genres.

---

## Tools & Libraries
- Python 🐍  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Google Colab  

---

## Steps Performed
1. **Data Loading** – Imported CSV dataset into Pandas DataFrame.  
2. **Data Cleaning** – Remove duplicates, handle missing values, convert data types.  
3. **Exploratory Analysis** – Summary statistics, top categories, free vs paid apps.  
4. **Visualization** – Bar charts, histograms, scatter plots, heatmaps.  
5. **Conclusions** – Key insights summarized below.

---

## Key Insights / Conclusions
- **Ratings:** Most apps rated between 4.0–4.5; few low-quality apps exist.  
- **Categories:** Family, Games, Tools have highest app counts; Health & Finance have higher average ratings.  
- **Installs:** Free apps generally have more installs than paid; top categories with millions of installs: Games, Communication, Social.  
- **Reviews:** High review count ≠ high rating.  
- **Price vs Rating:** Most paid apps < $5; price doesn’t strongly correlate with rating.  
- **Correlations:** Reviews positively correlate with installs; ratings less correlated with popularity.

---

## How to Use
1. Open in **Google Colab**:  
[Open Notebook](https://colab.research.google.com/github/shafiq73/2024/blob/main/05_complete_EDA_google_playstore_data.ipynb)  
2. Run cells step by step to reproduce analysis.  
3. Modify dataset path or add your own analysis.

---

## Future Work
- Predict app ratings using machine learning  
- Analyze sentiment from reviews  
- Build interactive dashboard for categories & revenue

---

## Author
**Shafiq Ahmed**  
GitHub: [shafiq73](https://github.com/shafiq73)
