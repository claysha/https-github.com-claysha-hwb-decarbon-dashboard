import streamlit as st
import pandas as pd
import subprocess
from eco_behavior_score_updated import calculate_eco_score_from_logs
from carbon_intensity_api import fetch_current_carbon_intensity
from eco_tips import get_latest_eco_tip

st.set_page_config(page_title="Decarbonization Dashboard", layout="wide")

def decarbonization_dashboard():
    st.title("EV Decarbonization Dashboard")

    # Grid CO2 Intensity
    carbon_data = fetch_current_carbon_intensity()
    st.subheader("Grid Carbon Intensity (UK)")
    st.metric("Current CO₂ Intensity", f"{carbon_data['actual']} gCO₂/kWh")

    # Eco Score Section
    eco_score, co2_intensity = calculate_eco_score_from_logs()
    st.subheader("Eco Driving Score")
    st.metric("Eco Score", f"{eco_score}/100")

    # Log Button
    st.subheader("Log This Trip")
    if st.button("Log This Trip"):
        result = subprocess.run(["python3", "eco_logger.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Trip successfully logged to eco_log.csv.")
        else:
            st.error("Failed to log trip. See logs for more details.")
            st.text(result.stderr)

    # GHG Savings
    try:
        df = pd.read_csv("ghg_log.csv", parse_dates=["timestamp"])
        total_saved = df["co2_savings_kg"].sum()
        st.subheader("GHG Emissions Avoided")
        st.metric("Total CO₂ Saved", f"{total_saved:.2f} kg")
        st.line_chart(df.set_index("timestamp")["co2_savings_kg"])
    except Exception as e:
        st.error(f"Error loading GHG log: {e}")

    # Eco Score Trend
    try:
        eco_df = pd.read_csv("eco_log.csv", parse_dates=["timestamp"])
        st.subheader("Eco Score Over Time")
        st.line_chart(eco_df.set_index("timestamp")["eco_score"])
    except Exception as e:
        st.warning("No eco_log.csv found or data incomplete.")

    # Smart Eco Tips
    st.subheader("Smart Eco Tips")
    tips = get_latest_eco_tip()
    for tip in tips:
        st.info(tip)

if __name__ == "__main__":
    decarbonization_dashboard()