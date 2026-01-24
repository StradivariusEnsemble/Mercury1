import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
st.title("Mercury Notebook No1")
st.caption("a simple study of health activity and risk levels by your truly Magento Kubiza")
df1 = pd.read_csv("HealthActivity.csv")
df2 = pd.read_csv("HealthRisk.csv")
st.subheader("Hours of sleep and heart rate dispayed by gender")
st.bar_chart(df1, x="Hours_of_Sleep", y=["Heart_Rate"],color ="Gender") 
st.subheader("Correlation between weight and BMI dispayed by age")
st.bar_chart(df1, x="Weight_kg", y="BMI", color="Age")
st.subheader("Health Risk")
st.caption("based on biomedical parameters")
fig2 = sns.pairplot(df2, hue="Risk_Level")
st.pyplot(fig2)
