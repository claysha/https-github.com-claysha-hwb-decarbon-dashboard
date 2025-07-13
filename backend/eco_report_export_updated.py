
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt
import os

def plot_and_save_chart(data, x_col, y_col, title, filename):
    plt.figure()
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def export_eco_report():
    date_str = datetime.now().strftime("%Y-%m-%d")
    pdf_name = f"eco_report_{date_str}.pdf"
    csv_name = f"eco_report_{date_str}.csv"

    try:
        df = pd.read_csv("eco_log.csv", parse_dates=["timestamp"])
        df.to_csv(csv_name, index=False)

        # Generate plots
        if not df.empty:
            plot_and_save_chart(df, "timestamp", "eco_score", "Eco Score Over Time", "eco_score_plot.png")
            plot_and_save_chart(df, "timestamp", "co2_intensity", "Charging CO₂ Intensity", "co2_plot.png")

        # Load ghg_log for GHG savings plot
        ghg_df = pd.read_csv("ghg_log.csv", parse_dates=["timestamp"])
        if not ghg_df.empty:
            plot_and_save_chart(ghg_df, "timestamp", "co2_savings_kg", "GHG Savings Over Time", "ghg_plot.png")

        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Eco Driving Report - {date_str}", ln=True, align="C")
        pdf.ln(10)

        # Insert plots
        for chart in ["eco_score_plot.png", "co2_plot.png", "ghg_plot.png"]:
            if os.path.exists(chart):
                pdf.image(chart, w=180)
                pdf.ln(10)

        pdf.output(pdf_name)
        print(f"[✓] Exported {pdf_name} and {csv_name}")
        return pdf_name, csv_name

    except Exception as e:
        print(f"[X] Failed to export: {e}")
        return None, None

if __name__ == "__main__":
    export_eco_report()
