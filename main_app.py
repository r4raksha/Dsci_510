import pandas as pd
import streamlit as st 

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'merged1.csv'  # Adjust the file path to your CSV file
df = load_data(file_path)

st.sidebar.info("DSCI 510 Final Project")

# Main layout
tabs = st.sidebar.radio('Navigation', ['Introduction', 'Research Questions', 'Data Sources', 'Data and visualizations'])

if tabs == 'Introduction':
    st.title("Introduction")
    st.write('Name: Raksha Ravichandran')
elif tabs == 'Research Questions':
    st.title("Research Questions")
    st.write('This is the Research Questions tab.')
elif tabs == 'Data Sources':
    st.title("Data Sources")
    st.write('This is the Data Sources tab.')
elif tabs == 'Data and visualizations':
    st.title("Data and Visualizations")
    st.write('This is the Data Visualization tab.')
    start_year = st.sidebar.selectbox('Select Start Year', df['Year'].unique())
    end_year = st.sidebar.selectbox('Select End Year', df['Year'].unique())
    start_month = st.sidebar.selectbox('Select Start Month', df['Month'].unique())
    end_month = st.sidebar.selectbox('Select End Month', df['Month'].unique())
    show_data = st.sidebar.checkbox('Show Data')
    # Filter data based on user selection
    filtered_df = df[
        (df['Year'] >= start_year) & (df['Year'] <= end_year) & 
        (df['Month'] >= start_month) & (df['Month'] <= end_month)
    ]

    # Display filtered data if checkbox is selected
    if show_data:
        st.subheader('Filtered Data')
        st.write(filtered_df)
