import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(file_path)

if selected_tab == 'Introduction':
    st.write('This is the Introduction tab.')
elif selected_tab == 'Research Questions':
    st.write('This is the Research Questions tab.')
elif selected_tab == 'Dataframe':
    st.write(df)  # Display the DataFrame here
elif selected_tab == 'Data and visualizations':
    st.write('This is the Data and visualizations tab.')

# @st.cache  # This line caches the function result
# def load_data(file_path):
#     return pd.read_csv(file_path)

# file_path = 'merged1.csv'
# df = load_data(file_path)

# # Sidebar widgets
# # search_term = st.text_input('Search Real Estate Stock', '')

# main_tab, research_questions, data_sources, data_vis = st.columns(4)
# tabs = st.radio('Navigation', ['Introduction', 'Research Questions', 'Data Sources', 'Data and visualizations'])

# if tabs == 'Introduction':
#     main_tab.write('This is the Introduction tab.')
# elif tabs == 'Research Questions':
#     research_questions.write('This is the Research Questions tab.')
# elif tabs == 'Data Sources':
#     data_sources.write('This is the Data Sources tab.')
# elif tabs == 'Data and visualizations':
#     start_year = st.sidebar.selectbox('Select Start Year', df['Year'])
#     end_year = st.sidebar.selectbox('Select End Year', df['Year'])
#     show_data = st.sidebar.checkbox('Show Data')

#     # Filter data based on user selection
#     filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

#     # Display filtered data
#     if show_data:
#         data_vis.subheader('Filtered Data')
#         data_vis.write(filtered_df)