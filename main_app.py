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
    st.markdown("My webapp contains the following four pages: Introduction, Research Questions, Dataframe, and Data and Visualizations.")
    st.markdown("\t     I. To navigate my webapp, begin at the Introduction! This page is an overview of takeaways from my plots, tables, and its interactivity as well as my conclusions from the visualizations. I also reflected on the project findings and process on this page.") 
    st.markdown("\t    II. The second page contains more in-depth reflection questions which have a few explanations as to what I discovered, challenges, skills I wish I had for the project, and future direction and steps.")
    st.markdown("\t   III. Next, on the Dataframe page, I listed all three sources and described how I acquired the datasets for my project, from web scraping the FRED website to utilizing the stock market and interest rate API’s.")
    st.markdown("\t    IV. The final page shows each visualization I’ve made and their interactivity from the datasets!")
    
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

    xmin = 2005
    xmax = 2022

    chart = alt.Chart(df).mark_circle().encode(
        x='Year',
        y='CPI',
        update_yaxes(range=[ymin, ymax]),
    ).interactive()

    chart = chart.configure_scale(
        x=alt.Scale(domain=[xmin, xmax])
    )

    tab1, tab2 = st.tabs(["CPI (Consumer Price Index) over the Years", "Graph Description"])
    with tab1:
        st.altair_chart(chart, theme = None, use_container_width=True)
    with tab2:
        st.markdown("This visualization shows how Consumer Price Index is around the same range throughout each month. My follow-up question to this was observing the years and seeing overall impact during the recession years.")

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
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.markdown("Graph Description")

    fig = px.line(filtered_df, x='Year', y='lifeExp', color='country', markers=True)
    fig.show()

    
