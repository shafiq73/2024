# 🛸 Spaceship Titanic: Interstellar Survival Prediction

### Advanced Machine Learning Pipeline for Kaggle’s Space-Themed Challenge

---

## 🌌 Project Overview

In the year 2912, the **Spaceship Titanic** encountered a catastrophic space-time anomaly, resulting in passengers being transported to an alternate dimension.

This project leverages machine learning to predict which passengers were affected, using structured data recovered from the ship’s damaged systems.

Beyond prediction, the project demonstrates how **data science can uncover hidden patterns in complex, real-world-like datasets**, combining storytelling with advanced analytics.

---

## 🎯 Objectives

* Build a high-performance binary classification model
* Apply advanced feature engineering techniques
* Extract meaningful insights from complex tabular data
* Ensure model generalization using cross-validation
* Develop a clean, reproducible ML pipeline

---

## 🛠️ Tech Stack & Tools

* **Python**
* **Pandas & NumPy** → Data manipulation
* **Matplotlib & Seaborn** → Visualization
* **Scikit-learn** → Machine learning models
* **XGBoost** → High-performance gradient boosting
* **Jupyter Notebook** → Interactive development

---

## 🧬 Data Engineering & Feature Innovation

This project stands out due to its **advanced feature engineering strategy**:

### ❄️ CryoSleep & VIP Analysis

* Strong correlation between CryoSleep status and transportation
* Behavioral segmentation of VIP vs non-VIP passengers

### 🏠 Cabin Decomposition

* Extracted **Deck, Cabin Number, and Side (Port/Starboard)**
* Captures spatial positioning within the spaceship

### 💳 Spending Behavior Features

* Aggregated luxury expenses:

  * RoomService
  * FoodCourt
  * ShoppingMall
  * Spa
  * VRDeck
* Helps identify passenger lifestyle and class

### 🧠 Smart Missing Value Handling

* Group-based imputation using similar passenger profiles
* Preserves data patterns better than simple mean/median

---

## ⚙️ Machine Learning Strategy

A multi-model approach was used for robust performance:

* **Logistic Regression** → Interpretable baseline
* **Random Forest** → Handles non-linear relationships
* **XGBoost** → Optimized for high accuracy and performance

### 🔁 Cross-Validation

* Implemented **K-Fold Cross-Validation**
* Ensures model reliability on unseen data

---

## 📊 Key Insights from Exploratory Data Analysis

* ❄️ **CryoSleep Effect**
  Passengers in CryoSleep had significantly higher transportation probability

* 🌍 **Home Planet Influence**
  Passengers from Europa exhibited distinct behavioral patterns

* 💰 **Spending Behavior**
  Lower spending correlated with higher transportation likelihood

* 🧭 **Spatial Patterns**
  Cabin location (Deck & Side) played a meaningful role

---

## 🏗️ Code Architecture & Pipeline Design

The project follows a clean, modular pipeline:

### 1. Data Preprocessing

* Missing value handling
* Data cleaning and transformation

### 2. Regex-Based Feature Extraction

* Extract Deck and Room Number from Cabin
* Convert raw text into structured features

### 3. Encoding & Dimensionality

* One-Hot Encoding for categorical variables
* Avoidance of multicollinearity (dummy variable trap)

### 4. Model Training & Evaluation

* Multiple classifiers trained and compared
* Evaluation using accuracy and classification metrics

---

## 📈 Model Performance Summary

| Model               | Type              | Strength                 |
| ------------------- | ----------------- | ------------------------ |
| Logistic Regression | Linear Model      | Fast & interpretable     |
| Random Forest       | Ensemble Learning | Handles complex patterns |
| XGBoost             | Gradient Boosting | Highest performance      |

---

## 🚀 How to Run

### 1. Clone Repository

```id="s82ksd"
git clone https://github.com/shafiq73/2024.git
```

### 2. Navigate to Project

```id="p29sld"
cd 2024
```

### 3. Run Notebook

Open `Keggle002_Spaceship_Titanic_main.ipynb` in Jupyter Notebook or Google Colab and execute all cells.

---

## 🏁 Final Insights & Conclusion

* **CryoSleep** emerged as one of the strongest predictors
* **Passenger behavior and spending patterns** significantly influenced outcomes
* **Cabin-based spatial features** improved model accuracy
* Ensemble models outperformed linear approaches

---

## ✨ Final Outcome

A robust and scalable machine learning pipeline capable of transforming complex, noisy data into **accurate and actionable predictions**.

This project demonstrates strong capabilities in:

* Data preprocessing
* Feature engineering
* Model building
* Real-world problem solving

---

## 🌟 Future Enhancements

* Hyperparameter tuning (GridSearchCV / Optuna)
* Feature importance dashboards
* Deep learning experimentation
* Deployment as a web application (Streamlit / Django)

---

## 👨‍💻 Author

**Shafiq Ahmed**
🔗 GitHub: https://github.com/shafiq73

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ and sharing your feedback!

---

### 🚀 “Exploring Data Beyond Earth — Turning Space Complexity into Predictive Intelligence”
