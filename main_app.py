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
tabs = st.sidebar.radio('Navigation', ['Introduction', 'Research Questions', 'Data Sources', 'Data and Visualizations'])

if tabs == 'Introduction':
    st.title("Introduction")    
    st.subheader("Name: Raksha Ravichandran")
    st.markdown("My webapp contains the following four pages: **Introduction, Research Questions, Dataframe, and Data and Visualizations.**")
    st.markdown("1) To navigate my webapp, begin at the Introduction! This page is an overview of takeaways from my plots, tables, and its interactivity as well as my conclusions from the visualizations. I also reflected on the project findings and process on this page.") 
    st.markdown("2) The second page contains more in-depth reflection questions which have a few explanations as to what I discovered, challenges, skills I wish I had for the project, and future direction and steps.")
    st.markdown("3) Next, on the Dataframe page, I listed all three sources and described how I acquired the datasets for my project, from web scraping the FRED website to utilizing the stock market and interest rate API’s.")
    st.markdown("4) The final page shows each visualization I’ve made and their interactivity from the datasets!")

    st.markdown("**Plots/Charts**")
    st.markdown("Scatter Plot of Interest Rate and Consumer Price Index (CPI): For my first plot, I looked at the relationship of the key parameters, CPI and mainly interest rate, and its relation to the years of 2009 to 2021. CPI is obtained from officialdata.org/us/stocks and the interest rate from FRED API. The values can be interpreted as the end of each month (December), as shown as yellow in the legend and hover display. Overall, this graph is used to identify interest rate trends in the economy.")
    st.markdown("Line Graph of American Tower Revenue: For this second visualization, I observed the correlation of the revenue of the top grossing real estate investment trust (REIT) to the years of 2009 to 2021. This is webscraped from the macrotrend.net website and depicts the various months using the toggle to display each month's change in revenue. This graph displays the revenue of American Tower (AMT), obtained from macrotrends.net.")  
    st.markdown("Bar Plot for Return Rate: For my third graph, I found how many times a specific percentage value of return rate appeared by displaying its count as an x-value and using the hovertemplate to display the return rate's year as the y-value. Return Rate Percentage represents the stock performance, whether it declines or grows in value, and is webscraped from officialdata.org/us/stocks.")
    st.markdown("Plotting CPI, Interest Rate, REIT revenue: I plotted all three factors, CPI, REIT revenue, interest rate and its association to stock performance (return rate percentage). This portrays the relationships with emphasis on the years of recession around 2009 and 2021.")
    
    st.markdown("**Conclusions**")
                
    st.markdown("**Major Gotchas**")
    
elif tabs == 'Research Questions':
    st.title("Research Questions")
    st.markdown("**1. What I set out to study (the point of my project):**")
    st.markdown("The main goal of my project is to find how the revenue of major real estate companies with stocks in the United States (which are known as real estate investment trusts) correlate to stock performance over the years. I also was interested to see how interest rates affected the stock performance, as an indicator of decline or growth. The years of interest were 2009 after the recession and 2021 after the COVID-19 pandemic since these years showed significant decline in the stock market, and are valuable benchmarks for overall housing market trends. During this project, however, I was not able to combine all the datsets I had set out for Milestone 2. I removed the webscraped datasets of the rest of the top 5 grossing REIT revenues (prologis, crown castle, digital, and public storage) and also short-term interest rate data because the dataset was too large to upload and deploy on Github.")
    st.markdown("My project addresses the following questions:")
    st.markdown("1a) How do long-term interest rates affect the stock market (return rate)? It aims to understand how fluctuations in interest rates influence stock market performance? It aims to understand how fluctuations in interest rates influence stock market performance.")
    st.markdown("1b) How does stock performance affect real estate? Before and after the years of 2008 (the Great Recession) and 2020 (COVID-19)? This seeks to uncover how changes in stock performance correlate with real estate trends during these periods.")

    st.markdown("**2. What I discovered from my project:**")
    st.markdown("I discovered that there is a weak, but positive correlation between stock market performance growth and consumer price index increase, and vice versa. There is also correlation between the stock market peformance growth and long-term interest rates. However, I could not draw many conclusions from the housing market and stock market return percentage.")
    
    st.markdown("**3. Difficulties I had in completing my project:**")
    st.markdown("Finding websites that were API-accessible for both my initial project plan and my final submission was challenging. It was also difficult for me to combine all the datasets I wanted to merge into one. Github would not allow me to upload large files, so I had to narrow it down from short-term interest rate and the other 4 top grossing REITs to soley long-term interest rate and highest grossing REIT for revenue, making my dataset less robust.")
    
    st.markdown("**4. Skills I wish I had while doing the project:**")
    st.markdown("It was challenging to deploy streamlit, especially with not understanding the requirements.txt and getting used to its features. I had a difficult time just getting started from scratch on my webapp, so I would've liked to have greater expertise in this area of the project. I also struggled with the API access with my inital project idea, so I would've liked to gain more knowledge on this aspect.")
    
    st.markdown("**5. Future steps to expand/augment my project:**")
    st.markdown("Some future steps I would use to expand my project are combining the datasets which I had to remove for my final submission, such as merging more REITs and other factors on stock performance which contribute to the real estate stock market, such as short term interest rates or even mortgage rates. I would consider conducting further analysis on how strong of a correlation the relationships are with R-squared coefficient and calculating significant difference with analytical T-tests. I was not able to make strong conclusions on the housing market, however, since I used only one source of revenue from one REIT, so I would also test more REITs in future steps.")
    
elif tabs == 'Data Sources': 
    st.title("Data Sources")
    st.write("Brief Description of Data: My data contains 6 columns and 3,745 rows and was created by merging Interest Rate, Revenue, CPI, Month, Return (%), at the common variable, 'Year'. It contains years ranging from 2009 to 2021. By utilizing this dataset, multi-faceted relationships were discovered by first examining each variable (Consumer Price Index (CPI), Long Term Interest Rate, and American Tower Revenue) over the years, and then comparing overall patterns in relation to stock performance (Return Rate %).")
    st.markdown("1) API: The API used was from the Federal Reserve Economic Data website. I obtained the dataset from the long-term interest rate federal funds data.")
    st.markdown("2) Webscraping website: I webscraped the macrotrends.net website for American Tower Revenue, Month, and Year.")
    st.markdown("3) Webscraping website: I also webscraped the officialdata.org/us/stocks for S&P 500 stocks and derived the Return (%), Month, and Year.")
                
elif tabs == 'Data and Visualizations':
    st.title("Data and Visualizations")
    st.write('The following tabs display my visualizations and final observations on the project. Hovering over each data point is possible to identify specific values in the visualization. There is also interactivity on the sidebar to filter data for groups of interest on the dataset I used for the project. Adjust the start and end of the month and year and click "Show Data" to invoke interactivity.')
    
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
        color="Month",
        size_max=20,
    )

    tab1, tab2 = st.tabs(["Plotting Interest Rate, Month, and Year", "Graph Description"])
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
    
    tab1, tab2 = st.tabs(["Line Graph of American Tower Revenue from 2009 - 2021", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")

    fig = px.bar(df, x='Year', y='Return (%)',
             hover_data=['Year', 'Return (%)'], 
             height=500)
    fig.show()

    tab1, tab2 = st.tabs(["Bar Plot of Return Rate over the Years", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")

    
    df_melt = df.melt(id_vars='Year', value_vars=['Revenue', 'Interest Rate', 'CPI', 'Return (%)'])
    fig = px.line(df_melt, x='Year' , y='value' , color='variable')

    tab1, tab2 = st.tabs(["Revenue, Interest Rate, CPI, and Return % over the Years", "Graph Description"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("Graph Description")


    
    

    
