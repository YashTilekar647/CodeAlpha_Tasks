
# Car Price Prediction with Machine Learning

This project demonstrates how to predict car prices using machine learning models.  It utilizes a dataset of car attributes and their corresponding prices to train and evaluate models, ultimately deploying a simple Flask API for predictions.



## Introduction

Predicting car prices is a valuable application of machine learning.  This project explores this by using various car features, such as engine size, horsepower, and mileage, to predict the price.  We use popular Python libraries like pandas, scikit-learn, and Flask to build and deploy the model.

## Prerequisites

Before running the project, ensure you have Python installed and the following libraries:

pip install pandas numpy matplotlib seaborn scikit-learn Flask
Dataset

The dataset used in this project is the Car Price Dataset, available on Kaggle.  You can download it from [Kaggle - Car Price Dataset](Kaggle Link) or use the provided URL in the code to download it directly.

#Data Preprocessing
The data preprocessing steps include:

#Dropping irrelevant columns (e.g., CarName).
Converting categorical features into numerical representations using one-hot encoding.
Handling missing values (if any).
Feature Selection and Data Splitting
We select relevant features for training and split the dataset into training (80%) and testing (20%) sets.

#Model Training
Two machine learning models are trained:

#Linear Regression
Random Forest Regressor
Model Evaluation
The models are evaluated using Root Mean Squared Error (RMSE) and R-squared (R²) score.

#Model Saving
The trained Random Forest model is saved using pickle for later use.

#Model Loading and Usage
The saved model can be loaded and used to predict car prices for new data.

#Flask API Deployment
A Flask API is created to allow users to interact with the model and get predictions by sending POST requests with car features.

#Project Structure
Car_Price_Prediction/
├── car_price_prediction.py  # Main script
├── car_price_model.pkl      # Saved model
├── app.py                   # Flask API
├── requirements.txt         # Dependencies
├── README.md                # Documentation
└── dataset.csv              # Car price dataset

How to Run
1.Clone the repository: git clone https://github.com/your-username/your-repo.git
2.Navigate to the project directory: cd Car_Price_Prediction
3.Install the required libraries: pip install -r requirements.txt
4.Run the Flask API: python app.py
5.Send a POST request to the API endpoint /predict with car features in JSON format.
Contributing
Contributions are welcome!  Please open an issue or submit a pull request.