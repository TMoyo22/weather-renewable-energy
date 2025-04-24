import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load dataset
csv_path = "C:/Users/tatem/Desktop/weather-renewable-energy/Dataset/Renewable.csv"
df = pd.read_csv(csv_path)

# Preprocess date column
df["Time"] = pd.to_datetime(df["Time"])
df.set_index("Time", inplace=True)

# Add month and year columns for filtering
df["month"] = df.index.to_series().dt.month
df["year"] = df.index.to_series().dt.year

# Streamlit page setup
st.title("\U0001F4C8 Time-Series Analysis of Solar Energy Generation")
st.markdown("""
This page analyzes how solar energy output (Energy Delta) varies over time, based on key environmental variables. We focus on the relationships between Sunlight Time, GHI, Day Length, and Energy Delta to understand trends and improve solar energy forecasting.
""")

# Interactive filters
st.sidebar.header("Filter Data")
year_options = ["Overall"] + sorted(df["year"].unique().tolist())
month_options = ["Overall"] + sorted(df["month"].unique().tolist())

selected_year = st.sidebar.selectbox("Select Year", options=year_options)
selected_month = st.sidebar.selectbox("Select Month", options=month_options)

filtered_df = df.copy()
if selected_year != "Overall":
    filtered_df = filtered_df[filtered_df["year"] == selected_year]
if selected_month != "Overall":
    filtered_df = filtered_df[filtered_df["month"] == selected_month]

# Line graph over time
st.markdown("## \U0001F4C9 Time Trends")
fig2_1, ax5 = plt.subplots(figsize=(10, 5))
filtered_df[["Energy delta[Wh]", "GHI", "sunlightTime"]].plot(ax=ax5)
ax5.set_title("Figure 2.1 - Time Trend of Energy, GHI, and Sunlight Time")
ax5.set_ylabel("Values")
st.pyplot(fig2_1)

# Seasonal Decomposition
st.markdown("## \U0001F50D Seasonal Decomposition of Energy Delta")
df_daily = df["Energy delta[Wh]"].resample("D").mean().dropna()
decomposition = seasonal_decompose(df_daily, model="additive", period=365)

fig2_2 = decomposition.trend.plot(title="Figure 2.2 - Trend Component", figsize=(10, 3)).get_figure()
st.pyplot(fig2_2)

fig2_3 = decomposition.seasonal.plot(title="Figure 2.3 - Seasonal Component", figsize=(10, 3)).get_figure()
st.pyplot(fig2_3)

fig2_4 = decomposition.resid.plot(title="Figure 2.4 - Residual Component", figsize=(10, 3)).get_figure()
st.pyplot(fig2_4)

# Summary text
st.markdown("""
### \U0001F9E0 Summary: Connecting Time-Series Analysis to the Research
- Solar energy generation is **strongly dependent on sunlight exposure**, confirmed by correlations between sunshine duration, GHI, and energy delta.
- **Summer months** (Dec–Jan) offer longer days and better energy output opportunities.
- **Decomposition graphs** break down energy production trends and identify hidden seasonal effects and external disruptions.
- These insights validate the need for **predictive and adaptive solar energy systems**, enhancing both performance and efficiency.
""")
