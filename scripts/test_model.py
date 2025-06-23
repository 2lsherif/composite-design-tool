import pandas as pd
import joblib

# Load model
model = joblib.load("models/recommender.pkl")

# Load the training dataset
df = pd.read_csv("data/composite_training_data.csv")

# Keep only numeric columns (same as model was trained on)
df = df.select_dtypes(include=["number"])

# Drop the target column to get only features
X = df.drop(columns=["score"])

# Take the first row as sample input
sample = X.iloc[[0]]

# Predict
predictions = model.predict(sample)
print(f"✅ Predicted score for sample input: {predictions[0]:.2f}")
