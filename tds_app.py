import streamlit as st

st.subheader("Find Largest Number")

st.write("Enter the numbers:")
num1 = st.number_input("Number 1",min_value=0,step=1)
num2 = st.number_input("Number 2",min_value=0,step=1)
num3 = st.number_input("Number 3",min_value=0,step=1)

 
if(num1>num2):
  largest = num1
else:
  largest = num2

if (num3 >largest):
  largest = num3

st.write("Largest Number: " +largest)
