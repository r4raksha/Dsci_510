import pandas as pd
import streamlit as st 
import altair as alt
import plotly.express as px

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
    st.subheader("Name: Raksha Ravichandran")
    st.markdown("My webapp contains the following four pages: **I. Introduction, II. Research Questions, III. Dataframe, and IV. Data and Visualizations.**")
    st.markdown("\t     I. To navigate my webapp, begin at the Introduction! This page is an overview of takeaways from my plots, tables, and its interactivity as well as my conclusions from the visualizations. I also reflected on the project findings and process on this page.") 
    st.markdown("\t    II. The second page contains more in-depth reflection questions which have a few explanations as to what I discovered, challenges, skills I wish I had for the project, and future direction and steps.")
    st.markdown("\t   III. Next, on the Dataframe page, I listed all three sources and described how I acquired the datasets for my project, from web scraping the FRED website to utilizing the stock market and interest rate API’s.")
    st.markdown("\t    IV. The final page shows each visualization I’ve made and their interactivity from the datasets!")

    st.markdown("**Plots/Charts**")
    st.markdown("**Conclusions**")
    st.markdown("**Major Gotchas**")
    
elif tabs == 'Research Questions':
    st.title("Research Questions")
    st.write('The points below reflect on the progress of my project:')

    st.markdown("**1. What I set out to study (the point of my project): **")
    st.markdown("**2. What I discovered from my project: **")
    st.markdown("**3. Difficulties I had in completing my project: **")
    st.markdown("**4. Skills I wish I had while doing the project: **")
    st.markdown("**5. Future steps to expand/augment my project: **")
    
elif tabs == 'Data Sources': 
    st.title("Data Sources")
    st.write("Brief description of data/API (what it contains, what it represents, etc.):")
    st.write("Q4: Briefly (4-6 sentence) describe how you might combine these datasets (i.e. how do they relate to each other?  What are the commonalities between them?  How might you connect them?  How do they enrich each other?). For example, if you scraped census data that contains a person’s “home town”, google maps API data, and data with median income per zip code, you might discuss how you would use the google maps API to translate the hometown to a particular zip code, and then combine that with the income data.")  
    st.write("G5: Briefly (4-6 sentence) describe what you might hope to find in the data overall.  Basically, what are you trying to accomplish in this research project?  What relationship are you trying to explore, or what pattern are you trying to discover, etc.")

elif tabs == 'Data and visualizations':
    st.title("Data and Visualizations")
    st.write('The following tabs display my visualizations and final observations on the project. There is also interactivity on the sidebar to filter data for groups of interest on the dataset I used for the project. Adjust the start and end of the month and year and click "Show Data" to invoke interactivity.')
    
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

    fig = px.scatter(
        df,
        x="Year",
        y="Interest Rate",
        size="CPI",
        color="Month",
        size_max=20,
    )

    tab1, tab2 = st.tabs(["Plotting CPI, Interest Rate, Month, and Year", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")
    
    fig = px.line(
        df, 
        x='Year', 
        y='Revenue', 
        color='Month', 
        markers=True)
    fig.show()
    
    tab1, tab2 = st.tabs(["Line Graph of Stock Performance", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")

    fig = px.scatter(
        df, 
        x="Year", 
        y="CPI")
    fig.show()

    tab1, tab2 = st.tabs(["Scatter Plot of American Tower Revenue from 2009 - 2021", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")
    

    
