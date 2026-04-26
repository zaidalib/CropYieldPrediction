# 📝 **Note**
This project was created for academic submission for the subject 'Intro To ML'

---

# 🌾 Crop Yield Prediction

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

> A Machine Learning web application that predicts crop yield (hg/hectare) based on environmental and agricultural factors — built with Random Forest and deployed via Streamlit.

---

## 📌 Overview

Agriculture drives economies. This project uses historical crop and weather data from **28,242 records across multiple countries (1990–2013)** to train a regression model that predicts how much yield a crop will produce given:

- 🌍 Country / Region
- 🌱 Crop Type
- 🌧️ Annual Rainfall (mm)
- 🌡️ Average Temperature (°C)
- 🧪 Pesticide Usage (tonnes)
- 📅 Year

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link.streamlit.app)

> Replace the link above with your actual Streamlit deployment URL after deploying.

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Random Forest Regressor |
| R² Score | **0.9857** |
| MAE | 3,752.48 hg/ha |
| RMSE | 10,181.76 hg/ha |
| Training Size | 22,593 records |
| Test Size | 5,649 records |

---

## 🧠 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| #1 | Crop Type (Item) | ~60% |
| #2 | Pesticides (tonnes) | ~11% |
| #3 | Avg Temperature | ~10% |
| #4 | Rainfall (mm/year) | ~9% |
| #5 | Country (Area) | ~5% |
| #6 | Year | ~2% |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.x |
| ML Model | Scikit-learn — RandomForestRegressor |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Serialization | Pickle |
| Development | Jupyter Notebook |

---

## 📁 Project Structure

```
crop-yield-prediction/
│
├── app.py                  # Streamlit web application
├── crop_yield.ipynb        # Jupyter notebook (training pipeline)
├── crop_yield_model.pkl    # Trained Random Forest model
├── le_area.pkl             # LabelEncoder for Area column
├── le_item.pkl             # LabelEncoder for Item column
├── requirements.txt        # Python dependencies
└── datasets/
    └── yield_df.csv        # Merged dataset (source: Kaggle)
```

---

## ⚙️ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/crop-yield-prediction.git
cd crop-yield-prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## 📦 Dataset

- **Source:** [Kaggle — Crop Yield Prediction Dataset](https://www.kaggle.com/)
- **Records:** 28,242
- **Features:** Area, Item, Year, Rainfall, Pesticides, Temperature
- **Target:** `hg/ha_yield` (hectograms per hectare)
- **Missing Values:** None

---

## 📈 How It Works

```
User Input (Area, Crop, Year, Rainfall, Pesticides, Temp)
        ↓
LabelEncoder (converts Area & Crop to integers)
        ↓
Random Forest Regressor (100 decision trees)
        ↓
Predicted Yield (hg/hectare)
```

---

## 📄 License

This project is for academic purposes only.
