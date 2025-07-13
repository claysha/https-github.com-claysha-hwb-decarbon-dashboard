
import streamlit as st
import pandas as pd
from eco_behavior_score_updated import calculate_eco_score_from_logs
from carbon_intensity_api import fetch_current_carbon_intensity
from eco_tips import get_latest_eco_tip

st.set_page_config(page_title="HWB Decarbonization Dashboard", layout="wide")

st.title("🌱 HWB Decarbonization Dashboard")

# Live Carbon Intensity
carbon_data = fetch_current_carbon_intensity()
st.metric("Current Grid CO₂ Intensity", f"{carbon_data['actual']} gCO₂/kWh")

# Eco Score
eco_score, _ = calculate_eco_score_from_logs()
st.metric("Eco Driving Score", f"{eco_score}/100")

# GHG Log
st.subheader("GHG Savings Over Time")
try:
    ghg_df = pd.read_csv("ghg_log.csv", parse_dates=["timestamp"])
    st.line_chart(ghg_df.set_index("timestamp")["co2_savings_kg"])
except:
    st.warning("GHG log not found or incomplete.")

# Eco Score Trend
st.subheader("Eco Score Trend")
try:
    eco_df = pd.read_csv("eco_log.csv", parse_dates=["timestamp"])
    st.line_chart(eco_df.set_index("timestamp")["eco_score"])
except:
    st.warning("Eco log not found or incomplete.")

# Smart Eco Tips
st.subheader("💡 Smart Eco Tips")
for tip in get_latest_eco_tip():
    st.info(tip)
