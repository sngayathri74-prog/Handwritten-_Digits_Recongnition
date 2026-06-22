import streamlit as st

st.title("Letter Counter")

text = st.text_input("Enter a sentence")

if text:
    count = len(text.replace(" ", ""))
    st.write("Total Letters:", count)
