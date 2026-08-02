import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Read Excel File
df = pd.read_excel(r"C:\Users\D-TECH POINT\Downloads\house_price_dataset.xlsx")

# Features
X = df[["Area", "Bedrooms", "Age"]]

# Target
y = df["Price"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")