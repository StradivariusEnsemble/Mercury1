import streamlit as st
import pandas as pd
import plotly.express as px
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
    fig_hist = px.histogram(
        df,
        x='Daily Water Intake (liters)',
        nbins=40,
        marginal='box',
        title='Distribution of Daily Water Intake (liters)'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    st.divider()

    st.subheader("Weight vs Intake by Physical Activity Level")
    fig_scatter = px.scatter(
        df,
        x='Weight (kg)',
        y='Daily Water Intake (liters)',
        color='Physical Activity Level',
        hover_data=['Age', 'Gender', 'Hydration Level'],
        title='Weight vs Daily Water Intake'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.divider()

    st.subheader("Hydration Level Distribution")
    counts = df['Hydration Level'].value_counts().reset_index()
    counts.columns = ['Hydration Level', 'count']
    fig_pie = px.pie(counts, names='Hydration Level', values='count', title='Hydration Level Distribution')
    st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()


    st.subheader("Hydration Level Correlations")
    #st.caption("based on biomedical parameters")
    fig4 = sns.pairplot(df, hue="Hydration Level")
    st.pyplot(fig4)