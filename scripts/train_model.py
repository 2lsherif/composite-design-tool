import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


# Load data
df = pd.read_csv("data/composite_training_data.csv")

# Drop all non-numeric columns (e.g. names, references)
df = df.select_dtypes(include=["number"])

# Split features and target
X = df.drop(columns=["score"])
y = df["score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/recommender.pkl")

print("✅ Model saved at models/recommender.pkl")
