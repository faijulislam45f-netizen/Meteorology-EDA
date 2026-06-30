# India Temperature EDA (1901-2024)

Climate change analysis using Python, Pandas, and Plotly. Explores 124 years of India's monthly temperature data to uncover long-term warming trends.

## Dataset Overview

| Detail | Info |
|--------|------|
| Source | India Monthly Temperature Data |
| File | `raw_pre1.csv` |
| Rows | 124 (Years: 1901–2024) |
| Columns | 15 (Year, Jan–Dec, Winter, Season) |

## Key Findings

- **1901–1950 Avg Temp:** 24.56 °C
- **1951–2024 Avg Temp:** 24.95 °C
- **Temperature Rise:** +0.38 °C
- Post-1980, temperature anomalies are overwhelmingly positive — clear warming signal.

## Feature Engineering

- `Winter_Avg`, `Summer_Avg`, `Monsoon_Avg`, `PostMonsoon_Avg` — seasonal averages
- `Annual_Avg` — yearly mean temperature
- `Decade` — grouped by decade for trend analysis
- `Anomaly` — deviation from 1901–1950 baseline
- `Is_Extreme` — flags years above (mean + std)

## Visualizations

**1. Annual Temperature Trend (1901–2024)**
Line chart with 10-year rolling trend showing long-term warming pattern.

**2. Temperature Anomaly (Baseline: 1901–1950)**
Bar chart, color-coded red (warming) vs blue (cooling) — clearly shows post-1980 warming surge.

## Files

| File | Description |
|------|--------------|
| `temp_eda.py` | Data cleaning, feature engineering, analysis |
| `temp_visualizations.py` | Plotly charts (trend + anomaly) |
| `annual_trend.png` | Annual temperature trend chart |
| `anomaly.png` | Temperature anomaly chart |
| `raw_pre1.csv` | Raw dataset |

## Tools Used
Python, Pandas, Plotly Express, Kaleido
