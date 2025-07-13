
# ⚡ HWB Decarbonization Dashboard

Welcome to the **HWB Passenger-Facing Decarbonization Dashboard** — a real-time, cloud-hosted dashboard that tracks eco-driving behavior, carbon intensity, and greenhouse gas (GHG) savings.

🔗 **Live App**: [Visit on Streamlit](https://<your-app-url>.streamlit.app)  
📦 Auto-generated reports weekly via GitHub Actions

---

## 🔍 Features

- 📉 **Live Eco Score**: Based on your recent trip efficiency, smoothness, and charge CO₂ levels  
- 📈 **GHG Emissions Avoided**: Visualize how much CO₂ you’ve saved
- 📊 **Charts**: Trends in eco-driving, grid carbon intensity, and savings over time  
- 💡 **Smart Eco Tips**: Personalized suggestions for cleaner driving and charging
- 🗂️ **Weekly Reports**: Auto-exported PDF + CSV reports in the GitHub repo

---

## 📁 Key Files

| File                          | Description |
|-------------------------------|-------------|
| `streamlit_app.py`            | Streamlit Cloud dashboard |
| `eco_report_export.py`        | PDF + chart export script |
| `eco_logger.py`               | Trip logger for eco tracking |
| `ghg_log.csv` / `eco_log.csv` | Logged GHG savings + behavior |
| `.github/workflows/weekly_report.yml` | Weekly automation |

---

## 🚀 Deploy Your Own

To deploy to [Streamlit Cloud](https://streamlit.io/cloud):

1. Fork or clone this repo  
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → Click "New App"  
3. Point to `streamlit_app.py` and `main` branch  
4. Done! 🌍

---

## 📬 Contact

Questions or contributions welcome.  
Maintained by [`@claysha`](https://github.com/claysha)
