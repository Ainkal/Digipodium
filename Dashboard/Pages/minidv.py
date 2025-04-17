import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


st.title("Welcome to dashboard Mini Project")
df=pd.read_csv(r'C:\Users\atink\OneDrive\Desktop\Digipodium\Dashboard\assets\world_population.csv')

st.dataframe(df)

df

# Sidebar filters
st.sidebar.header("Filters")
countries = st.sidebar.multiselect("Select Countries", df["Country/Territory"].unique(), default=["India", "United States"])
year_range = st.sidebar.slider("Select Year Range", int(df["2000 Population"].min()), int(df["2020 Population"].max()), (2000, 2020))

# Filter data
filtered_df = df[(df["Country/Territory"].isin(countries)) & 
                 (df["2000 Population"] >= year_range[0]) & 
                 (df["2020 Population"] <= year_range[1])]

# Show filtered data
st.write("### Filtered Data", filtered_df)


fig1=px.line(filtered_df, x="2000 Population", y="2020 Population", color="Country/Territory", title="Population Over Years")
st.plotly_chart(fig1)