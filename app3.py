import streamlit as st
from PIL import Image 
st.title("Personal Bank Details")
st.text_input(" first Name")
st.text_input(" Middle Name")
st.text_input(" Surname")
st.selectbox("Title",['Miss','Mr','Mrs'])
st.radio("Gender",['Male','Female'])
st.date_input("D.O.B")
st.text_input("Phone Number")
st.selectbox("Bank Accounts",['Savings Account','Current Account','Salary Account','Eazysave Account','Children`s Account','Domiciliary Account','Loan'])
st.selectbox("Ways To Bank",['Online Banking','ATM','Mobile App',''])
st.text_area("Description",max_chars=150)
st.selectbox("Country",["Uk","US","Nigeria","Ghana"])
st.checkbox("Agree")
st.write("Submitted")
