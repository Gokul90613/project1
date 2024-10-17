import streamlit as st

st.title('sum of two number')

num = st.slider("number", 0, 130, 25)
num2 = st.slider("number",0,25)
sum = num+num2
st.write(f"The sum of {num} and {num2} is {sum}")