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
