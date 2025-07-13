
import pandas as pd

def get_latest_eco_tip(log_path="eco_log.csv"):
    try:
        df = pd.read_csv(log_path)
        latest = df.dropna(subset=["eco_score", "co2_intensity", "trip_distance_km", "energy_used_kwh"]).iloc[-1]

        tips = []

        # Eco score logic
        if latest["eco_score"] < 60:
            tips.append("Try smoother acceleration and deceleration to improve your eco score.")
        elif latest["eco_score"] < 80:
            tips.append("You're doing well! Maintain consistent speeds to score even higher.")

        # CO2 intensity logic
        if latest["co2_intensity"] and latest["co2_intensity"] > 180:
            tips.append("Charging during this time emits more CO₂. Try charging later if possible.")

        # Efficiency logic
        wh_per_km = (latest["energy_used_kwh"] * 1000) / latest["trip_distance_km"]
        if wh_per_km > 190:
            tips.append("Consider reducing speed and avoiding rapid acceleration to improve efficiency.")

        return tips or ["You're doing great — keep it up!"]
    except Exception as e:
        return [f"Unable to generate tip: {e}"]
