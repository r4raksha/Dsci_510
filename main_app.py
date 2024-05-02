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
    st.markdown("<h1 style='text-align: center;'>Food Aayush 🍲 🩺</h1>", unsafe_allow_html=True)
    
    st.subheader("About FoodAayush 🤔")

    #all the necessary descriptions
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial, sans-serif;line-height: 1.5;'>Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.</h6>", unsafe_allow_html=True)
    st.markdown("")
    st.subheader("Activity Diagram ♺")
    st.image('resources/about_process_diagram/1.png')

    st.markdown("")
    st.subheader("Classification of food items and cooking oils based on quality")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>Food becomes stale if there is excessive exposure to environmental factors such as heat and humidity. Similarly, if a cooking oil sample is exposed to heat, or is used in cooking repeatedly, it will become rancid. The second part of our application is the classification of food items based on their freshness and oils based on their rancidity. A classification model is developed for classifying food items into various freshness levels based on their visual properties. For oils, the classification is done on the basis of the visual properties as well as the pH value of the oil sample. The pH value is recorded using a pH sensor integrated with the application. These features are included in our mobile application which is developed using the Flutter toolkit.</h6>", unsafe_allow_html=True)
    
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
