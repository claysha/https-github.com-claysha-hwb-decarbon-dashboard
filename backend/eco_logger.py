
import csv
from datetime import datetime
import pandas as pd
from eco_behavior_score_updated import calculate_eco_score_from_logs
from carbon_intensity_api import fetch_current_carbon_intensity

def log_eco_score(
    behavior_log_path="behavior_log.csv",
    eco_log_path="eco_log.csv"
):
    try:
        df = pd.read_csv(behavior_log_path)
        latest = df.dropna(subset=["trip_distance_km", "energy_used_kwh"]).iloc[-1]

        distance_km = float(latest["trip_distance_km"])
        energy_kwh = float(latest["energy_used_kwh"])
        timestamp = latest["timestamp"]

        eco_score, co2_intensity = calculate_eco_score_from_logs()

        with open(eco_log_path, "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["timestamp", "eco_score", "co2_intensity", "trip_distance_km", "energy_used_kwh"])
            writer.writerow([timestamp, eco_score, co2_intensity, distance_km, energy_kwh])
        return True

    except Exception as e:
        print(f"Failed to log eco score: {e}")
        return False

if __name__ == "__main__":
    log_eco_score()
