import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px


st.title("Welcome to dashboard")
df=sns.load_dataset("titanic")
st.dataframe(df)



#Gender filter
gender=st.sidebar.multiselect('Gender',
                              options=df['sex'].unique(),
                              default=df['sex'].unique())

#age filter
age=st.sidebar.slider('Age',
                       min_value=int(df['age'].min()),
                       max_value=int(df['age'].max()),
                       value=(int(df['age'].min()),int(df['age'].max())))

#class filter

pclass=st.sidebar.multiselect('Class',
                                options=df['pclass'].unique(),
                                default=df['pclass'].unique())

filtered_data=df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) &
    (df['age'].between(age[0],age[1]))
]


filtered_data



#histogram of age distribution 
st.subheader("Age distribution")
fig=px.histogram(filtered_data,x="age",nbins=20,title="Age distribution")
st.plotly_chart(fig)


#piechart of survival rate by gender
fig=px.pie(filtered_data,names='sex',values='survived',title='Survival rate by gender ',color_discrete_sequence=['#FF9999','#66B3FF'],hole=0.5)
st.plotly_chart(fig)



#passenger count by class
#fig=px.bar(df,x="pclass",y="survived",title="Passenger count by class",color='survived',color_discrete_sequence=['red','blue'])  
#st.plotly_chart(fig)    

#survival rate by age
fig=px.line(filtered_data.groupby('age')['survived'].mean().reset_index(),x='age',y='survived',title="Survival rate by age",markers=True)
st.plotly_chart(fig)

