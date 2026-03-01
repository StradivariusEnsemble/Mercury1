import streamlit as st
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt 

dfB = pd.read_csv("heart_attack_dataset.csv")

n=333
list_df5 = [dfB[i:i+n] for i in range(0,len(dfB),n)]

df1A = list_df5[0]
df1B = list_df5[1]
df1C = list_df5[2]

st.title("Heart Risk Overview")

st.metric(label="Average Age", value=round(dfB['Age'].mean(),1))

tab1, tab2, tab3 = st.tabs(["Group A", "Group B", "Group C"])  
with tab1:
     st.caption("Test group A")
     figA = sns.jointplot(data=df1A, x="Blood Pressure (mmHg)", y="Cholesterol (mg/dL)", hue="Age")
     st.pyplot(figA)
with tab2:
     st.caption("Test group B")
     figB = sns.jointplot(data=df1B, x="Blood Pressure (mmHg)", y="Cholesterol (mg/dL)", hue="Smoking Status", kind="scatter")
     st.pyplot(figB)
with tab3:
     st.caption("Test group C")
     figC = sns.jointplot(data=df1C, x="Blood Pressure (mmHg)", y="Cholesterol (mg/dL)", hue="Gender", kind="scatter")
     st.pyplot(figC)

st.divider()

tab4, tab5, tab6 = st.tabs(["Group A", "Group B", "Group C"])  
with tab4:
     st.caption("Test group A")
     figD = sns.pairplot(df1A, hue="Treatment")
     st.pyplot(figD)
#dfD = dfB.drop(columns=["Chest Pain Type"])
with tab5:
     st.caption("Test group B")
     figE = sns.pairplot(df1B, hue="Treatment")
     st.pyplot(figE)
with tab6:
     st.caption("Test group C")
     figF = sns.pairplot(df1C, hue="Treatment")
     st.pyplot(figF)