import streamlit as st
import pandas as pd

# Uncomment to load data
@st.cache_data # This line caches the function result
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'merged1.csv'  # Adjust the file path to your CSV file
df = load_data(file_path)

st.sidebar.info("Raksha's Data 510 Project: Stock Market, Interest Rates, and Real Estate Revenue During Economic Recessions")

# Sidebar widgets
start_year = st.sidebar.selectbox('Select Start Year', df['Year'].unique())
end_year = st.sidebar.selectbox('Select End Year', df['Year'].unique())
show_data = st.sidebar.checkbox('Show Data')

# Main layout
main_tab, research_questions, data_sources, data_vis = st.columns(4)
tabs = st.radio('Navigation', ['Introduction', 'Research Questions', 'Data Sources', 'Data and visualizations'])

if tabs == 'Introduction':
    main_tab.write('This is the Introduction tab.')
elif tabs == 'Research Questions':
    research_questions.write('This is the Research Questions tab.')
elif tabs == 'Data Sources':
    data_sources.write('This is the Data Sources tab.')
elif tabs == 'Data and visualizations':
    data_vis.write('This is the Data Visualization tab.')
    # Filter data based on user selection
    #filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Display filtered data if checkbox is selected
    #if show_data:
        #data_vis.subheader('Filtered Data')
        #data_vis.write(filtered_df)
