
import pandas as pd
from fpdf import FPDF
from datetime import datetime

def export_eco_report(csv_path="eco_log.csv", export_csv="eco_report_export.csv", export_pdf="eco_report.pdf"):
    try:
        df = pd.read_csv(csv_path)

        # Export CSV
        df.to_csv(export_csv, index=False)
        print(f"[✓] CSV exported to {export_csv}")

        # Export PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Eco Driving Report", ln=True, align="C")
        pdf.cell(200, 10, txt=f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        pdf.ln(10)

        col_width = 40
        for col in df.columns:
            pdf.cell(col_width, 10, col, 1)
        pdf.ln()

        for _, row in df.iterrows():
            for item in row:
                pdf.cell(col_width, 10, str(item), 1)
            pdf.ln()

        pdf.output(export_pdf)
        print(f"[✓] PDF exported to {export_pdf}")

    except Exception as e:
        print(f"[X] Failed to export reports: {e}")

if __name__ == "__main__":
    export_eco_report()
