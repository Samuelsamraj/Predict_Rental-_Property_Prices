# Predict_Rental-_Property_Prices

# Real Estate Rent Prediction

## Problem Statement

In the real estate industry, determining the appropriate rental price for a property is crucial for property owners, tenants, and property management companies. Accurate rent predictions can help landlords set competitive prices, tenants make informed rental decisions, and property management companies optimize their portfolio management. The goal of this project is to develop a data-driven model that predicts the rental price of residential properties based on relevant features. By analyzing historical rental data and property attributes, the model aims to provide accurate and reliable rent predictions.

## Tools Used

- Python
- Jupyter Notebook
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, XGBoost, Category Encoders

## Approaches

1. **Data Preprocessing:**
   - Handling missing values
   - Imputation of missing data
   - Converting data types
   - Encoding categorical variables

2. **Exploratory Data Analysis (EDA):**
   - Visualizing property size distribution
   - Analyzing rent distribution
   - Correlation analysis
   - Exploring building types and property age

3. **Feature Engineering:**
   - Creating age categories for properties
   - Extracting month and day from activation date

4. **Modeling:**
   - Linear Regression
   - K Nearest Neighbor Regression
   - Decision Tree Regression
   - Random Forest Regression
   - Extreme Gradient Boosting Regression

5. **Evaluation:**
   - Cross-validation scores for each model
   - R2 scores for model evaluation

6. **Feature Importance:**
   - Utilizing XGBoost for feature importance
   - Visualizing feature importance

## EDA Insights

- Property size and the number of bedrooms show a strong positive correlation.
- Rent distribution is positively skewed, with a higher concentration in the lower to mid-range values.
- The most common building type is "Apartment," followed by "Independent House" and "Gated Community."
- The distribution of property ages is right-skewed, with a higher concentration of relatively newer properties.


