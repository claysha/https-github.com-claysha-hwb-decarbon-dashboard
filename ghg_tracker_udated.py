
import csv
from datetime import datetime
import pandas as pd

CO2_PER_KWH = 0.233  # kg CO2 per kWh (UK average)

def compute_savings_per_row(distance_km, energy_kwh):
    if distance_km == 0 or energy_kwh == 0:
        return 0.0
    actual_efficiency = (distance_km * 1000) / (energy_kwh * 1000)  # km per kWh
    baseline_efficiency = 5.0  # km per kWh
    baseline_energy = distance_km / baseline_efficiency
    improved_energy = energy_kwh
    saved_kwh = max(0, baseline_energy - improved_energy)
    return round(saved_kwh * CO2_PER_KWH, 3)

def process_log(input_csv="behavior_log.csv", output_csv="ghg_log.csv"):
    df = pd.read_csv(input_csv)
    df = df.dropna(subset=["trip_distance_km", "energy_used_kwh"])

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "co2_savings_kg"])

        for _, row in df.iterrows():
            timestamp = row["timestamp"]
            distance_km = float(row["trip_distance_km"])
            energy_kwh = float(row["energy_used_kwh"])
            savings = compute_savings_per_row(distance_km, energy_kwh)
            writer.writerow([timestamp, savings])

if __name__ == "__main__":
    process_log()
