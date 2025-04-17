import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


st.title("Welcome to dashboard Mini Project")
df=pd.read_csv(r'C:\Users\atink\OneDrive\Desktop\Digipodium\Dashboard\assets\world_population.csv')

st.dataframe(df)

df
# Step 1: Melt year-based columns
pop_cols = [col for col in df.columns if "Population" in col and col[0].isdigit()]
df_long = df.melt(id_vars=["Country/Territory", "Continent"], 
                  value_vars=pop_cols, var_name="Year", value_name="Population")

# Extract year as integer
df_long["Year"] = df_long["Year"].str.extract(r'(\d{4})').astype(int)


# Sidebar filters
st.sidebar.header("Filters")
countries = st.sidebar.multiselect("Select Countries", df["Country/Territory"].unique(), default=["India", "United States"])
year_range = st.sidebar.slider("Select Year Range", min_value=1970, max_value=2022, value=(2000, 2020))

# Filter the melted DataFrame
filtered_df = df_long[
    (df_long["Country/Territory"].isin(countries)) &
    (df_long["Year"] >= year_range[0]) &
    (df_long["Year"] <= year_range[1])
]

st.write("### Filtered Data", filtered_df)

fig1 = px.line(filtered_df, x="Year", y="Population", color="Country/Territory", markers=True,
               title="Population Growth Over Time")
st.plotly_chart(fig1, use_container_width=True)



fig7 = px.scatter(
    filtered_df,
    x="Year",
    y="Population",
    size="Population",  # Bubble size proportional to population
    color="Country/Territory",
    animation_frame="Year",
    range_y=[filtered_df["Population"].min(), filtered_df["Population"].max()],
    title="Animated Bubble Chart: Yearly Population Trends"
)
st.plotly_chart(fig7)


# Filter the original DataFrame for 2022 data
df_2022 = df.copy()
df_2022["Population"] = df_2022["2022 Population"]



fig8 = px.scatter_matrix(
    df_2022,
    dimensions=["Population", "Density (per km²)", "Growth Rate"],
    color="Continent",  # Differentiates points based on Continent
    hover_name="Country/Territory",
    title="Scatter Matrix: Population, Density, and Growth Rate (2022)"
)
st.plotly_chart(fig8)



fig9 = px.box(
    df,
    x="Continent",
    y="2022 Population",
    color="Continent",
    title="Box Plot: 2022 Population Distribution by Continent"
)
st.plotly_chart(fig9)
