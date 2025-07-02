from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("model/health_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    input_features = [
        data.get("age", 0),
        data.get("bp", 0),
        data.get("sugar", 0),
        data.get("chol", 0),
    ]
    prediction = model.predict([input_features])[0]
    return jsonify({"risk": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
