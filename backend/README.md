# EV HWB + SND Integrated Project

This project integrates two key subsystems:

✅ **Hybrid Water Box (HWB) Monitoring**
- Monitors EV battery SOC, water box level, anomalies, PoLA.
- Based on fused_battery_dataset.csv.

✅ **Spatial Navigable Detection (SND) + Visual Odometry (VO)**
- Detects drivable area and vehicle trajectory from camera inputs.

## 📂 Directory Structure

```
project/
├── hwb_pipeline/
│   ├── enhanced_pola_dashboard.py
│   ├── forecasting_module.py
│   └── …
├── snd_pipeline/
│   ├── snd_module.py
│   ├── vo_module.py
│   ├── deep_vo_module.py
│   └── pipeline_driver.py
├── datasets/
│   ├── fused_battery_dataset.csv
│   └── snd_datasets/
│       ├── scene1.png
│       └── video1.mp4
├── run_all.py
```

## 🚀 Run both pipelines

```bash
python run_all.py
```

Or run each individually:
```bash
streamlit run hwb_pipeline/enhanced_pola_dashboard.py
python snd_pipeline/pipeline_driver.py --input datasets/snd_datasets/video1.mp4 --method classical
```
