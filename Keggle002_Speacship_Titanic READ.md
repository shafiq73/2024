🛸 Spaceship Titanic: Interstellar Survival Prediction
Advanced Binary Classification for Kaggle's Space Mystery
🌌 Project Overview
The year is 2912. The spaceship Titanic collided with a space-time anomaly while transporting passengers to three nearby exoplanets. This project involves predicting which passengers were transported to an alternate dimension using a set of personal records recovered from the ship's damaged computer system.

🛠️ Data Engineering & Feature Innovation
This notebook implements a sophisticated data pipeline to handle complex interstellar data:

CryoSleep & VIP Analysis: Analyzed how being in "CryoSleep" significantly impacts survival/transportation rates.

Cabin Decomposition: Parsed the Cabin feature into Deck, Num, and Side (Port/Starboard) to understand the ship's spatial layout.

Spending Features: Aggregated luxury spending (RoomService, FoodCourt, ShoppingMall, Spa, VRDeck) to identify passenger demographics.

Handling Nulls: Used group-based imputation (filling missing values based on similar passenger profiles) rather than simple mean/median.

🤖 Modeling Strategy
To achieve high accuracy, I implemented a multi-model approach:

Random Forest Classifier: To handle non-linear relationships and high-dimensional categorical data.

XGBoost: For optimized gradient boosting, providing superior speed and performance.

Cross-Validation: Implemented K-Fold cross-validation to ensure the model generalizes well to unseen cosmic data.

📊 Key Insights from EDA
CryoSleep: Passengers in CryoSleep had a significantly higher probability of being transported.

HomePlanet: Passengers from Europa showed different transportation patterns compared to those from Earth or Mars.

Expenditure: Lower spenders were more likely to be transported, indicating a correlation with cabin location.

🚀 Installation & Usage
Clone the Repository:

Bash
git clone https://github.com/shafiq73/2024.git
Navigate to Project:
cd 2024

Run the Notebook:
Open Keggle002_Spaceship_Titanic_main.ipynb in any Jupyter environment.

Author: Shafiq
Building intelligent solutions for the future of space travel.
💻 Code Architecture & Logic
The project is structured into a modular pipeline to ensure reproducibility and clarity. Below is the breakdown of the core functional blocks:

1. Data Preprocessing & Cleaning
The preprocess() function serves as the central engine for data transformation.

Missing Value Imputation: Continuous variables like Age and Fare are filled using the mean to maintain the central tendency of the data.

Categorical Handling: For features like Embarked and Cabin, we introduce a new category ('X') to handle nulls without losing the row information.

2. Regex-Based Feature Engineering
We use Regular Expressions (Regex) to extract hidden patterns from the Cabin string:

df['Cabin'].str.extract(r'([A-Za-z]+)'): Isolates the Deck Letter, which indicates the passenger's vertical position on the ship.

df['Cabin'].str.extract(r'(\d+)'): Extracts the Room Number, helping the model identify clusters of passengers.

3. Dimensionality & Encoding
To prepare the data for Machine Learning algorithms:

One-Hot Encoding: Categorical variables (Sex, Embarked, Cabin_Letter) are converted into binary columns.

Redundancy Removal: We drop "dummy" columns like cabin_X to avoid the multi-collinearity trap (the "Dummy Variable Trap").

4. Model Training & Evaluation
We implement a competitive approach by training three distinct classifiers:

Logistic Regression: Provides a linear baseline for survival probability.

Random Forest: An ensemble of decision trees that captures complex interactions between features.

XGBoost: A high-performance gradient boosting framework optimized for Kaggle-style tabular data.

🏁 Conclusion & Final Insights
After rigorous testing and feature refinement, the following conclusions were drawn:

The "Women and Children First" Protocol: The data confirms that Gender was the most powerful predictor of survival. Female passengers had a significantly higher survival rate across all classes.

Socio-Economic Significance: Passenger Class (Pclass) and Fare showed a direct correlation with survival, suggesting that proximity to lifeboats and higher-deck accommodations played a vital role.

Feature Importance: The custom Deck Extraction from the Cabin data provided a measurable boost in model accuracy, proving that spatial location on the ship was a key survival factor.

Model Performance: While Logistic Regression provided a solid baseline (~78%), the XGBoost model emerged as the superior choice, effectively handling the non-linear nature of the Titanic dataset.

✨ Final Outcome
The final pipeline provides a robust framework for binary classification, successfully transforming raw historical records into a highly accurate predictive tool.
