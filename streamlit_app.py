import streamlit as st
import pandas as pd
import seaborn as sns
import os
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(os.path.join(os.getcwd(), "static","cdc.png"), width=300)
st.divider()
st.title("Mercury Notebook No1")
st.caption("a simple study of health activity and risk levels by your truly Magento Kubiza")
st.divider() 

df1 = pd.read_csv("HealthActivity.csv")
df2 = pd.read_csv("HealthRisk.csv")

n=333
list_df1 = [df1[i:i+n] for i in range(0,len(df1),n)]

df1A = list_df1[0]
df1B = list_df1[1]
df1C = list_df1[2]
st.subheader("Hours of sleep and heart rate dispayed by gender")
tab1, tab2, tab3 = st.tabs(["Group A", "Group B", "Group C"])  
with tab1:
    st.caption("test group A")
    st.bar_chart(df1A, x="Hours_of_Sleep", y=["Heart_Rate"],color ="Gender", stack="center")
with tab2:              
    st.caption("test group B")
    st.bar_chart(df1B, x="Hours_of_Sleep", y=["Heart_Rate"],color ="Gender", stack="center")
with tab3:
    st.caption("test group C")
    st.bar_chart(df1C, x="Hours_of_Sleep", y=["Heart_Rate"],color ="Gender", stack="center")
st.divider()
st.subheader("Correlation between Weight and BMI")
tab3, tab4, tab5 = st.tabs(["Group A", "Group B", "Group C"])  
with tab3:
     st.caption("Test group A")
     figA = sns.jointplot(data=df1A, x="Weight_kg", y="BMI", hue="Age")
     st.pyplot(figA)
with tab4:
     st.caption("Test group B")
     figB = sns.jointplot(data=df1B, x="Weight_kg", y="BMI", hue="Hours_of_Sleep", kind="scatter")
     st.pyplot(figB)
with tab5:
     st.caption("Test group C")
     figC = sns.jointplot(data=df1C, x="Weight_kg", y="BMI", hue="Gender", kind="hist", palette="rocket")
     st.pyplot(figC)
st.divider()
st.subheader("Health Risk")
st.caption("based on biomedical parameters")
df3=df2.drop(columns=["On_Oxygen", "O2_Scale"])
fig2 = sns.pairplot(df3, hue="Risk_Level")
st.pyplot(fig2)