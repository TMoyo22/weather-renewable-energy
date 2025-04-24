import streamlit as st
import pandas as pd
import os

st.title("🌞 Weather & Solar Energy Generation Analysis")

st.markdown("""
Understanding the relationship between weather conditions and energy generation is crucial for optimizing solar energy use.
This analysis focuses on how weather data affects Global Horizontal Irradiance (GHI) and Energy Delta.
""")

with st.expander("📄 Context and Problem Statement"):
    st.markdown("""
    **Problem Statement:**  
    Solar energy has greatly revolutionized the energy industry, as evidenced by its widespread adoption in the residential market. Despite this, solar intermittency and storage remain barriers to an optimal energy generation system (Team 2024).  
    Analyzing the effects of weather conditions on Global Horizontal Irradiance (GHI) and Energy Delta will assist us in gathering insights into the best daytimes, months, seasons, and conditions that generate the most useful energy (Energy Delta) from solar panels. Analysis of past trends will assist in creating a model that allows for the prediction of high and low usage phases to allow for energy storage planning, cutting costs and reducing energy wastage.  
    
    The `Renewable.csv` dataset (“Renewable Power Generation and Weather Conditions” 2024) from Kaggle would have utilized an IoT-based weather station fitted with temperature sensors, humidity sensors, photoresistors (to measure periods of sunlight), and other instruments for real-time feedback on weather conditions. This data, along with data from monitoring solar panel activity and energy usage, forms our key data sources.  
    
    To gain meaningful insights, we performed descriptive, prescriptive, and predictive analysis using Python (GeeksforGeeks 2025). Exploratory Data Analysis, time series forecasting, and multicollinearity analysis were all conducted to understand how various weather conditions affect energy production and storage.  
    
    The insights from this data will assist energy providers, businesses, solar users, and governments in making well-informed decisions on optimal storage utilization for more stable and sustainable energy consumption.
    """)

st.markdown("### 🧾 Dataset Preview")
st.markdown(
    """ To give an overview of the dataset, we will display the first 5 rows of the dataset using the `.head()` method. This will help us understand the structure and contents of the dataset before diving into the analysis. """
)

# Fixing the path to the CSV file
csv_path = os.path.join(os.getcwd(), "Dataset", "Renewable.csv")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.dataframe(df.head())
else:
    st.error(f"Could not find the file at `{csv_path}`. Please check the path.")
