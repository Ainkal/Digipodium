
#streamlit run calculator.py
import streamlit as st
st.title('Calculator')
st.markdown('Welcome to my web app')


c1,c2=st.columns(2)

#with c1:
#    num1=st.number_input('Enter first number')
#with c2:
#    num2=st.number_input('Enter second number')

num1=c1.number_input('Enter first number',value=0)
num2=c2.number_input('Enter second number',value=0)

task=st.radio('Select operation',['Addition','Subtraction','Multiplication','Division'])
result=0


if task=='Addition':
    result=num1+num2
elif task=='Subtraction':
    result=num1-num2
elif task=='Multiplication':
    result=num1*num2
elif task=='Division':
    result=num1/num2
else:
    st.error('Division by zero is not allowed')
    result=None

st.button('Calculate')
st.write(f'The result of {task} of {num1} and {num2} is {result}')