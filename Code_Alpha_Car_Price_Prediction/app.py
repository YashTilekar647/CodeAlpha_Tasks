from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "🚗 Car Price Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([data["features"]])  # Expecting JSON: {"features": [180, 120, 2800, 30]}
    prediction = model.predict(features)
    return jsonify({"predicted_price": f"${prediction[0]:,.2f}"})

if __name__ == "__main__":
    app.run(port=8000, debug=True)

