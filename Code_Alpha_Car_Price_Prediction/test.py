import requests

url = "http://127.0.0.1:8000/predict"
data = {"features": [180, 120, 2800, 30]}

response = requests.post(url, json=data, timeout=10)
print(response.json())  # Expected Output: {"predicted_price": "$18,500.00"}
