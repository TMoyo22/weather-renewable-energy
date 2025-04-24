import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


st.markdown("## 📊 Statistical Analysis of Weather Factors on Energy Generation")
st.markdown("""
We explore how **extreme weather conditions** impact solar energy output using statistical plots:

- **Violin and Boxplots** show distribution patterns.
- **Scatterplots and Correlation Heatmap** reveal linear relationships.
""")


# Load data
@st.cache_data
def load_data(path):
    return pd.read_csv(path)


csv_path = os.path.join(os.getcwd(), "Dataset", "Renewable.csv")

# --- Section 1: Distribution Analysis using Violin & Boxplots ---
st.subheader("🔍 Distribution of Energy Output under Weather Conditions")

cols = ["rain_1h", "snow_1h", "wind_speed"]
for col in cols:
    st.markdown(f"### {col.replace('_', ' ').title()} vs Energy Delta")
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    sns.violinplot(
        x=pd.cut(df[col], bins=[0, 0.1, 2, 5, 10, 50]),
        y=df["Energy delta[Wh]"],
        ax=axs[0],
    )
    axs[0].set_title(f"Violin Plot: {col}")
    axs[0].set_xlabel(f"{col} bins")
    axs[0].set_ylabel("Energy delta[Wh]")

    sns.boxplot(
        x=pd.cut(df[col], bins=[0, 0.1, 2, 5, 10, 50]),
        y=df["Energy delta[Wh]"],
        ax=axs[1],
    )
    axs[1].set_title(f"Box Plot: {col}")
    axs[1].set_xlabel(f"{col} bins")

    st.pyplot(fig)

# --- Section 2: Scatterplots for Specific Variables ---
st.subheader("📉 Weather Factor Trends with Energy Output")

scatter_cols = ["humidity", "temp", "pressure", "clouds_all"]
for col in scatter_cols:
    st.markdown(f"### Energy Delta vs {col.title()}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=col, y="Energy delta[Wh]", alpha=0.3, ax=ax)
    ax.set_title(f"{col.title()} vs Energy delta")
    st.pyplot(fig)

# --- Section 3: Correlation Heatmap ---
st.subheader("🧮 Correlation Heatmap")
correlation_features = [
    "Energy delta[Wh]",
    "humidity",
    "temp",
    "pressure",
    "clouds_all",
]
cor_matrix = df[correlation_features].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cor_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Correlation between Energy Delta and Weather Features")
st.pyplot(fig)

# --- Summary ---
st.markdown("### 📝 Conclusion Summary")
st.markdown("""
- **Rain/Snow/Wind**: Heavy values reduce energy output (confirmed by violin & boxplots).
- **Humidity & Clouds**: High levels correlate with **lower** energy.
- **Temperature**: Moderate temps (~10–20°C) are optimal.
- **Pressure**: Has **no significant effect** on energy output.
""")
