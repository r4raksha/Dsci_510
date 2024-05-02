pip freeze > requirements.txt

import streamlit as st
import pandas as pd
pip install matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('car_data.csv')
st.title('Car Data')
st.write(df)

# with st.sidebar:
  # st.write("Here is sidebar")

# Add a text input widget to the sidebar
car_name = st.sidebar.text_input("Enter car name:")
# Display a greeting message using the input from the sidebar
#st.write(f"Input the Car Name: {user_input}!")
