# 🩺 Smart Health Risk Predictor using ML

This project uses machine learning and a full stack web app (Flask + Streamlit) to predict the likelihood of a person being at health risk based on basic medical parameters.

## 🔧 Tech Stack:
- Backend: Flask, Scikit-learn
- Frontend: Streamlit
- Deployment Ready: Docker / Streamlit Cloud

## 🚀 Run Locally
```bash
# Backend
cd backend
python predict_api.py

# Frontend (new terminal)
cd frontend
streamlit run streamlit_app.py
```

## 👨‍🔬 Sample Input:
- Age: 45
- BP: 120
- Sugar: 170
- Chol: 220

## ✅ Output
"Prediction: ⚠️ At Risk"
