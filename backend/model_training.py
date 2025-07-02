import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("model", exist_ok=True)

df = pd.read_csv("../data/processed_cleveland_data.csv")

# Rename target column
df.rename(columns={"num": "target"}, inplace=True, errors='ignore')
df["target"] = (df["target"] > 0).astype(int)  # ensure binary

features = ["age","sex","cp","trestbps","chol","fbs","restecg",
            "thalach","exang","oldpeak","slope","ca","thal"]
X = df[features]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, "model/health_model.pkl")

print("✅ Model trained on real dataset and saved")
