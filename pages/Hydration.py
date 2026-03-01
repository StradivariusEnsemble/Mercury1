import streamlit as st
import pandas as pd
import seaborn as sns

df6 = pd.read_csv("Daily_Water_Intake.csv")

st.title("Daily Water Intake — Overview")


st.subheader("Summary")
mean_val = df6['Daily Water Intake (liters)'].mean()
median_val = df6['Daily Water Intake (liters)'].median()
std_val = df6['Daily Water Intake (liters)'].std()

st.metric(label="Average Daily Water Intake (liters)", value=round(df6['Daily Water Intake (liters)'].mean(),2))
st.metric(label="Standard Deviation (liters)", value=round(std_val,2))

st.divider()

st.subheader("Distribution")
st.bar_chart(df6, y = 'Daily Water Intake (liters)', x='Age', color='Gender')

st.divider()

st.subheader("Daily Water Intake for Weather condition by Hydration Level")
st.line_chart(df6, x='Weather', y='Daily Water Intake (liters)', color='Hydration Level')

st.divider()

st.subheader("Weight vs Intake by Physical Activity Level")
   
st.bar_chart(df6, x='Weight (kg)', y='Daily Water Intake (liters)', color='Physical Activity Level')

st.divider()

n =3333

list_df5 = [df6[i:i+n] for i in range(0,len(df6),n)]

df1A = list_df5[0]
df1B = list_df5[1]
df1C = list_df5[2]

st.subheader("Hydration Level Correlations")

tab1, tab2, tab3 = st.tabs(["Group A", "Group B", "Group C"])  

with tab1:
     st.caption("Test group A")
     fig5 = sns.pairplot(df1A, hue="Hydration Level", kind="kde")
     st.pyplot(fig5)
with tab2:
     st.caption("Test group B")
     fig6 = sns.pairplot(df1B,hue="Hydration Level", kind="kde")
     st.pyplot(fig6)
with tab3:
     st.caption("Test group C")
     fig7 = sns.pairplot(df1C, hue="Hydration Level", kind="kde")
     st.pyplot(fig7)