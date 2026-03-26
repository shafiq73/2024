🚢 Titanic: Survival Prediction AlphaAn End-to-End Machine Learning Pipeline for Kaggle's Premier Challenge📌 Executive SummaryThis repository contains a sophisticated machine learning workflow designed to solve the Titanic: Machine Learning from Disaster challenge. The project focuses on transforming raw, messy passenger data into actionable features to predict survival outcomes with high precision.🛠️ Tech Stack & ArchitectureThe FoundationsPandas & NumPy: For robust data manipulation and handling multidimensional arrays.Matplotlib: For exploratory data visualization (EDA).The ML EngineScikit-Learn: Powering the LogisticRegression baseline and RandomForest ensemble.XGBoost: Utilizing Gradient Boosting for state-of-the-art predictive performance.Preprocessing: Custom pipelines for automated missing value imputation and feature scaling.🧬 Feature Engineering HighlightsUnlike basic models, this notebook implements advanced Regex-based extraction to squeeze value out of the data:Cabin Decomposition: Extracted cabin_letter (Deck) and cabin_number to capture socio-economic positioning on the ship.Null Imputation Strategy: Applied mean-based filling for Age and Fare to maintain data distribution integrity.Categorical Encoding: Leveraged One-Hot Encoding for Sex and Embarked ports to eliminate categorical bias.📊 Model Comparison MatrixAlgorithmTypeStrengthLogistic RegressionLinearFast baseline for binary classification.Random ForestEnsembleHandles non-linear data and prevents overfitting.XGBoostBoostingOptimized for high-performance Kaggle rankings.🚀 How to ExecuteClone the Repo:Bashgit clone https://github.com/shafiq73/2024.git
Install Dependencies:Bashpip install numpy pandas matplotlib scikit-learn xgboost
Run the Notebook:Open Keggle001.ipynb in Jupyter or Google Colab and run all cells.📈 Future Roadmap[ ] Implement Hyperparameter Tuning using GridSearchCV.[ ] Add Feature Importance visualizations.[ ] Experiment with Stacking Classifiers to boost accuracy.Developed by Shafiq Turning data into insights, one row at a time.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# ---------------------------------------------------------
# Step 1: Model Training (Importance is generated post-training)
# ---------------------------------------------------------

# This step assumes you have used the preprocess() function to create:
# X_train_processed: Feature matrix (DataFrame)
# y_train: Target vector (Survival labels)

# --- BOILERPLATE TRAINING CODE (Replace with your actual variables) ---
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(X_train_processed, y_train.ravel()) 
# ------------------------------------------------------------------


# ---------------------------------------------------------
# Step 2: Extract Feature Importances
# ---------------------------------------------------------
# Random Forest includes an inbuilt 'feature_importances_' attribute.
importances = rf_model.feature_importances_

# Get the list of feature names in the same order as training
feature_names = X_train_processed.columns 

# Create a DataFrame for easy sorting and manipulation
feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})

# Sort the DataFrame in descending order (Most important features first)
feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False)


# ---------------------------------------------------------
# Step 3: Visualization (Feature Importance Bar Chart)
# ---------------------------------------------------------
plt.figure(figsize=(12, 8)) # Set a large canvas for clear label visibility

# Create a bar chart: Features on X-axis, Importance Score on Y-axis
plt.bar(feature_imp_df['Feature'], feature_imp_df['Importance'], color='teal')

# Set descriptive Labels and Title
plt.xlabel('Features', fontsize=12)
plt.ylabel('Importance Score', fontsize=12)
plt.title('🚢 Titanic Survival Prediction: Feature Importance (Random Forest)', fontsize=15)

# Rotate X-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid lines for easier visual comparison of values
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent clipping of text
plt.tight_layout() 
plt.show()

# ---------------------------------------------------------
# Step 4: Display Top Features in Text Format
# ---------------------------------------------------------
print("\n🔥 Top 5 Most Influential Features:")
print(feature_imp_df.head(5).to_string(index=False))
# X-axis ke labels ko rotate karein taaki wo readable ho (zyada features ke liye)
plt.xticks(rotation=45, ha='right')

# Grid lines add karein behtar readability ke liye
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Chart dikhayein
plt.tight_layout() # Layout ko adjust karein taaki kuch cut na jaye
plt.show()

# ---------------------------------------------------------
# Step 4: Top Features ko Print bhi Karein
# ---------------------------------------------------------
print("\n🔥 Top 5 Most Important Features:")
print(feature_imp_df.head(5).to_string(index=False))
Here is the comprehensive code to generate distinct Feature Importance visualizations for all three models you imported. The explanations and plot titles are entirely in English.

You can add these cells directly into your `Keggle001.ipynb` notebook after the model training section.

***

### 🛠️ Prerequisite: Standard Setup for All Plots
*Ensure this cell runs first so the variables are defined for the subsequent plotting cells.*

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Assuming your preprocessed training data is stored in these variables:
# X_train_processed (DataFrame), y_train (Series/Array)
# And assuming you have already defined and fitted your models:
# logreg_model, rf_model, xgb_model
```

***

### 📈 Plot 1: Logistic Regression Coefficients (Feature Impact)
Logistic Regression doesn't have "importance" in the same way trees do; instead, it has **coefficients**. These tell you the *direction* (positive = increases survival chance, negative = decreases) and *magnitude* of each feature's effect.

```python
# ---------------------------------------------------------
# Step 1: Extract Coefficients
# ---------------------------------------------------------
# Logistic Regression coefficients are in .coef_[0]
coefficients = logreg_model.coef_[0]
feature_names = X_train_processed.columns

# Create a DataFrame for sorting
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})

# Sort by absolute value to get the strongest predictors first
coef_df['AbsCoefficient'] = coef_df['Coefficient'].abs()
coef_df = coef_df.sort_values(by='AbsCoefficient', ascending=False).drop(columns=['AbsCoefficient'])

# ---------------------------------------------------------
# Step 2: Visualize Coefficients
# ---------------------------------------------------------
plt.figure(figsize=(12, 8))

# Define colors: Blue for positive impact, Red for negative impact
colors = ['#1f77b4' if c > 0 else '#d62728' for c in coef_df['Coefficient']]

plt.barh(coef_df['Feature'], coef_df['Coefficient'], color=colors)

# Labels and Title
plt.xlabel('Coefficient Value (Direction & Magnitude)', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.title('🚢 Titanic Survival: Logistic Regression Feature Coefficients', fontsize=15)

# Add a vertical line at zero
plt.axvline(x=0, color='black', linestyle='--', linewidth=1)

# Invert Y-axis to show the strongest predictors at the top
plt.gca().invert_yaxis()

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

print("\n📋 Top 5 Strongest Predictors (Logistic Regression):")
print(coef_df.head(5).to_string(index=False))
```

***

### 🌲 Plot 2: Random Forest Feature Importance (Gini Importance)
This shows how much each feature contributes to reducing impurity (making nodes cleaner) across all trees in the forest.

```python
# ---------------------------------------------------------
# Step 1: Extract Importances
# ---------------------------------------------------------
importances_rf = rf_model.feature_importances_
feature_names = X_train_processed.columns

# Create a DataFrame for sorting
rf_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances_rf})

# Sort by importance descending
rf_imp_df = rf_imp_df.sort_values(by='Importance', ascending=False)

# ---------------------------------------------------------
# Step 2: Visualize Importances
# ---------------------------------------------------------
plt.figure(figsize=(12, 8))

# Use a distinct color palette
plt.barh(rf_imp_df['Feature'], rf_imp_df['Importance'], color='#2ca02c') # Forest Green

# Labels and Title
plt.xlabel('Importance Score (Gini)', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.title('🚢 Titanic Survival: Random Forest Feature Importance', fontsize=15)

# Invert Y-axis to show the most important at the top
plt.gca().invert_yaxis()

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

print("\n🔥 Top 5 Most Important Features (Random Forest):")
print(rf_imp_df.head(5).to_string(index=False))
```

***

### 🚀 Plot 3: XGBoost Feature Importance (Gain)
For XGBoost, "Gain" is the most common metric. It implies the relative information that a feature brings to the model. We use XGBoost's native plotting utility for efficiency.

```python
from xgboost import plot_importance

# ---------------------------------------------------------
# Step 1: Visualize Importance directly using XGBoost utility
# ---------------------------------------------------------
# 'gain' is usually the most informative importance type
fig, ax = plt.figure(figsize=(12, 10)), plt.gca()

# Use the native XGBoost plotting function
plot_importance(xgb_model, ax=ax, importance_type='gain', color='#ff7f0e', title=None) # Orange

# Customize the plot
plt.title('🚢 Titanic Survival: XGBoost Feature Importance (Gain)', fontsize=15)
plt.xlabel('F-Score (Gain Importance)', fontsize=12)
plt.ylabel('Features', fontsize=12)

# Adjust layout to prevent label clipping
plt.tight_layout()
plt.show()
```

### Summary of What These Plots Show:

1.  **Logistic Regression:** Shows **weight and direction**. Example: `Sex_male` will likely have a strong negative coefficient (meaning being male decreased survival chance).
2.  **Random Forest:** Shows **predictive power**. It doesn't tell you "good" or "bad" for survival, just that the model relies heavily on that feature to make decisions.
3.  **XGBoost:** Shows **efficiency/gain**. It highlights which features were best at splitting the data to reduce the loss function most effectively.
4.  Model,Algorithm Type,Key Strength,Typical Accuracy
Logistic Regression,Linear Classifier,Excellent baseline; highly interpretable.,~78-80%
Random Forest,Ensemble (Bagging),Robust to outliers; prevents overfitting.,~81-83%
XGBoost,Gradient Boosting,Optimized for high-speed & Kaggle rankings.,~83-85%+

