import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import seaborn as sns


@st.cache_data
def load_data(path="Daily_Water_Intake.csv"):
    return pd.read_csv(path)


df = load_data()

st.title("Daily Water Intake — Overview")

if df.empty:
    st.warning("No data found in Daily_Water_Intake.csv")
else:
    st.subheader("Summary")
    mean_val = df['Daily Water Intake (liters)'].mean()
    median_val = df['Daily Water Intake (liters)'].median()
    std_val = df['Daily Water Intake (liters)'].std()

    c1, c2, c3 = st.columns(3)
    c1.metric("Mean (L)", f"{mean_val:.2f}")
    c2.metric("Median (L)", f"{median_val:.2f}")
    c3.metric("Std (L)", f"{std_val:.2f}")

    st.divider()

    st.subheader("Distribution")
    fig_hist = go.Figure(data=[go.Histogram(x=df['Daily Water Intake (liters)'], nbinsx=20)])
    st.plotly_chart(fig_hist, use_container_width=True)

    st.divider()

    st.subheader("Daily Water Intake for Weather condition by Hydration Level")
    st.line_chart(df, x='Weather', y='Daily Water Intake (liters)', color='Hydration Level')

    st.divider()

    st.subheader("Weight vs Intake by Physical Activity Level")
   
    st.bar_chart(df, x='Weight (kg)', y='Daily Water Intake (liters)', color='Physical Activity Level')

    st.divider()

    st.subheader("Hydration Level Correlations")
    #st.caption("based on biomedical parameters")
    fig4 = sns.pairplot(df, hue="Hydration Level")
    st.pyplot(fig4)