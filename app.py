import streamlit as st
import pickle
import numpy as np

# ── Load model & encoders ──────────────────────────────────────
model    = pickle.load(open("crop_yield_model.pkl", "rb"))
le_area  = pickle.load(open("le_area.pkl", "rb"))
le_item  = pickle.load(open("le_item.pkl", "rb"))

# ── UI ────────────────────────────────────────────────────────
st.title("🌾 Crop Yield Predictor")
st.write("Predict expected crop yield based on environmental factors.")

area  = st.selectbox("Country / Area", le_area.classes_)
item  = st.selectbox("Crop Type", le_item.classes_)
year  = st.slider("Year", 1990, 2030, 2010)
rain  = st.number_input("Rainfall (mm/year)", min_value=0.0, value=1000.0)
pest  = st.number_input("Pesticides (tonnes)", min_value=0.0, value=5000.0)
temp  = st.number_input("Avg Temperature (°C)", min_value=0.0, value=20.0)

if st.button("Predict Yield"):
    area_enc = le_area.transform([area])[0]
    item_enc = le_item.transform([item])[0]
    
    features = np.array([[area_enc, item_enc, year, rain, pest, temp]])
    prediction = model.predict(features)[0]
    
    st.success(f"Estimated Yield: **{prediction:,.0f} hg/ha**")
    st.caption("hg/ha = hectograms per hectare (divide by 10,000 for tonnes/ha)")