# 🚗 Car Price Prediction with Machine Learning 🚀

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("car_price.csv")

# Data Exploration
print(df.head())  # View first few rows
print(df.info())  # Check data types and missing values
print(df.describe())  # View summary statistics

# Data Preprocessing
# Display column names
print("Columns in dataset:", df.columns)

# Use correct categorical columns for encoding
categorical_columns = ['Fuel_Type', 'Selling_type', 'Transmission']  # Corrected column names

# Apply one-hot encoding
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
print("✅ Successfully encoded categorical columns:", categorical_columns)

# Select Features & Target
# Using appropriate features for prediction
X = df[['Year', 'Present_Price', 'Driven_kms', 'Owner', 'Fuel_Type_Petrol', 'Selling_type_Individual', 'Transmission_Manual']]
y = df['Selling_Price']

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Models
lr_model = LinearRegression()
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

lr_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

# Model Evaluation
y_pred_lr = lr_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))
rf_rmse = np.sqrt(mean_squared_error(y_test, y_pred_rf))

lr_r2 = r2_score(y_test, y_pred_lr)
rf_r2 = r2_score(y_test, y_pred_rf)

print(f"Linear Regression: RMSE = {lr_rmse:.2f}, R² Score = {lr_r2:.2f}")
print(f"Random Forest: RMSE = {rf_rmse:.2f}, R² Score = {rf_r2:.2f}")

# Save the Best Model
best_model = rf_model if rf_r2 > lr_r2 else lr_model

with open("car_price_model.pkl", "wb") as file:
    pickle.dump(best_model, file)

print("✅ Model saved as car_price_model.pkl")

# Load Model and Make Predictions
with open("car_price_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Example: Predict price for a new car
new_car = np.array([[2017, 8.5, 30000, 0, 1, 0, 1]])  # [Year, Present_Price, Driven_kms, Owner, Fuel_Type_Petrol, Selling_type_Individual, Transmission_Manual]
predicted_price = loaded_model.predict(new_car)

print(f"💰 Predicted Car Price: ${predicted_price[0]:,.2f}")
