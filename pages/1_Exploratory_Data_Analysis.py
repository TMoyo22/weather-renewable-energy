import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import os
import io


csv_path = "/Dataset/Renewable.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    st.error(f"❌ Could not find the file at `{csv_path}`. Please check the path.")

st.title("🔍 Exploatory Data Analysis of Weather Data")
st.markdown("""
    This section focuses on the exploratory data analysis (EDA) of the weather data. EDA is a crucial step in understanding the dataset, identifying patterns, and preparing for further analysis. We will explore the relationships between different weather variables and their impact on energy generation.
    """)

st.markdown("### 📊 Data Overview")
st.markdown("""
    We will start by understanding contents of the dataset.
    This includes the columns in the dataset, their data types, and any missing values.
    """)

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.markdown(
    "The dataset has no missing values, which is great for analysis and modeling !!"
)

st.markdown("### 📈 Descriptive Statistics")
st.dataframe(df.describe())


st.markdown("### 🧪 Correlation Analysis")
st.markdown("""
    The correlation matrix shows the correlation coefficients between different weather variables and energy generation metrics.
    """)

fig, ax = plt.subplots(figsize=(12, 6))
sb.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)


st.markdown("### 🌞 View Distribution of Selected Variable")
selected_col = st.selectbox(
    "Choose a variable", ["GHI", "Energy delta[Wh]", "temp", "dayLength", "humidity"]
)
color_map = {
    "GHI": "orange",
    "Energy delta[Wh]": "green",
    "temp": "red",
    "dayLength": "blue",
    "humidity": "black",
}

fig, ax = plt.subplots(figsize=(8, 5))
sb.histplot(df[selected_col], kde=True, ax=ax, color=color_map[selected_col])
ax.set_title(f"Distribution of {selected_col}")
st.pyplot(fig)
