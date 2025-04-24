import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from models import load_data, prepare_data, train_models, evaluate_model

st.title("🤖 Predictive Analysis of Solar Energy Generation")

# Load your data and models
csv_path = "C:\\Users\\tatem\\Desktop\\weather-renewable-energy\\Dataset\\Renewable.csv"
df = load_data(csv_path)
X_train, X_test, y_train, y_test = prepare_data(df)
models = train_models(X_train, y_train)

# Intro Section
st.markdown("""
We trained three regression models to predict solar energy generation based on weather data:
- **Linear Regression** – A basic approach assuming a linear relationship between features and target.
- **Decision Tree Regressor** – A tree-based model that learns decision rules from the data.
- **Random Forest Regressor** – An ensemble of decision trees for more robust predictions.

Each model was trained using all relevant weather features to predict the target variable `Energy delta[Wh]`.  
We evaluate each model's predictions using Mean Absolute Error (MAE) and Mean Squared Error (MSE).
""")

# Model Selector
model_choice = st.selectbox(
    "🔍 Select a model to view predictions", list(models.keys())
)

# Evaluate selected model
y_true, y_pred, mae, mse = evaluate_model(models[model_choice], X_test, y_test)

# Plot actual vs predicted

# Scatter plot: Actual vs Predicted
st.markdown("### 🔬 Scatter Plot: Actual vs Predicted")
fig2, ax2 = plt.subplots()
ax2.scatter(y_true, y_pred, alpha=0.5, color="teal")
ax2.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], "r--", lw=2)
ax2.set_xlabel("Actual Energy delta [Wh]")
ax2.set_ylabel("Predicted Energy delta [Wh]")
ax2.set_title(f"{model_choice} - Actual vs Predicted Scatter")
st.pyplot(fig2)

# Display metrics
st.markdown("### 📊 Model Performance")
st.markdown(f"**Mean Absolute Error (MAE)**: `{mae:.2f}`")
st.markdown(f"**Mean Squared Error (MSE)**: `{mse:.2f}`")
