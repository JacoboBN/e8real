import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df=pd.read_csv("airbnb.csv")

st.title("Airbnb Analysis")

st.dataframe(df.head())

st.subheader("Top Hosts in Madrid")

df_host = df.groupby(["host_id","host_name"]).size().reset_index()
df_host_sorted=df_host.sort_values(by=0, ascending=False).head(10)

st.dataframe(df_host_sorted)

fig=px.bar(df_host_sorted, x="host_name", y=0)

st.plotly_chart(fig)

# Selecting top hosts

host_selection=st.radio("how many hosts do you want to visualize?", [5,10,20, 50])
st.dataframe(df_host.sort_values(by=0, ascending=False).head(host_selection))


fig=px.bar(df_host_sorted, x="host_name", y=0)  
st.plotly_chart(fig, key="visualizacion de ejemplo")