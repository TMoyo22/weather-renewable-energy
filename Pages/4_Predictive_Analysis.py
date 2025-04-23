import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import os
import io

st.title("🤖 Predictive Analysis of Solar Energy Generation")

# Intro Section
st.markdown("""
We trained three regression models to predict solar energy generation based on weather data:
- **Linear Regression** – A basic approach assuming a linear relationship between features and target.
- **Decision Tree Regressor** – A tree-based model that learns decision rules from the data.
- **Random Forest Regressor** – An ensemble of decision trees for more robust predictions.

Each model was trained using the `hour` and `month` features to predict the target variable `Energy delta[Wh]`.  
We evaluate each model's predictions using Mean Absolute Error (MAE) and Mean Squared Error (MSE).
""")

# Model Selector
model_choice = st.selectbox(
    "🔍 Select a model to view predictions",
    ["Linear Regression", "Decision Tree", "Random Forest"],
)


y_true = np.array([100, 200, 150, 300, 250])
predictions = {
    "Linear Regression": np.array([110, 190, 160, 280, 240]),
    "Decision Tree": np.array([105, 205, 145, 290, 260]),
    "Random Forest": np.array([98, 198, 152, 302, 248]),
}

# Plot actual vs predicted
st.markdown("### 📈 Actual vs Predicted Values")
fig, ax = plt.subplots()
ax.plot(y_true, label="Actual", marker="o")
ax.plot(predictions[model_choice], label=f"Predicted - {model_choice}", marker="x")
ax.set_title(f"{model_choice} Prediction")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Energy delta [Wh]")
ax.legend()
st.pyplot(fig)

# Evaluation Metrics (dummy values — replace with real ones)
mae_values = {"Linear Regression": 12.4, "Decision Tree": 10.1, "Random Forest": 6.8}
mse_values = {"Linear Regression": 220.5, "Decision Tree": 180.2, "Random Forest": 95.3}

st.markdown("### 📊 Model Performance")
st.markdown(f"**Mean Absolute Error (MAE)**: {mae_values[model_choice]}")
st.markdown(f"**Mean Squared Error (MSE)**: {mse_values[model_choice]}")
