#############################################################################
# This project is ///
# Course: Interactive Data Science(05839-A)
# Coded By: Jeffrey Na, Ninad Bandewar
# AndrewID: jjna, nbandewa
# Date: Oct 09, 2022
# Thanks to Prof. John Stamper, Prof. Adam Perer & TAs for there assistance


#############################################################################
# Library Imports
#############################################################################
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#from vega_datasets import data

#############################################################################
# Data Import
#############################################################################
st.set_page_config(layout = "wide")


st.header('Seattle building energy analysis')
st.subheader('Introduction')
st.write("Buildings contribute to 38% of global emissions as per the UN Environmental Global Status Report 2020. Hence, it is crucial for us to make efforts to reduce energy consumption. Each building’s energy usage is mentioned in its monthly bill. However, it is quite challenging to assess if this amount would be higher/lower than others or the set average (threshold) consumption value for say, the 2050 goal. This can be achieved using the benchmark data. To be specific, Seattle has State Policies to require all public, commercial, and multifamily buildings to complete the benchmarking report of energy consumption in the building. In this regard, this app can be used to identify energy efficient buildings to learn more about practices responsible for its efficiency and also to identify buildings that perform poorly. This will help the owners or other parties for further analysis and assess if the building must be retrofitted with newer green attributes like more energy efficient appliances, better heating/cooling systems, airtight construction, etc to reduce its energy consumption.")


@st.cache
def load(url):
    return pd.read_csv(url, encoding = "latin1")

df = load("https://raw.githubusercontent.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/main/Combined.csv")

if st.checkbox("Show Raw Data"):
    st.write(df)

st.subheader("The following map plots all the buildings in the raw data based on the filter below")
selectMapFilter = st.selectbox("Which feature would you like to use to filter?",("EUI","EnergyStar"))
placeholder1 = st.empty()
placeholder1.line_chart({"data": [1, 5, 2, 6]})
st.write("The building you have selected has a 380 EUI and energy star score of 54 in the year 2020")

##1st chapter
st.subheader("1.Trend over the years of the selected buidling")

col11, col22 = st.columns(2)

with col11:
    st.write("1.a. What are the trends in energy consumption of my selected buildings across five years?")
    selectTrendFilter = st.selectbox("Which feature would you like to use to compare your building?",("Program Type","Zipcode"))

    #placeholder to be replaced with visuals
    placeholder2 = st.empty()
    placeholder2.line_chart({"data": [1, 5, 2, 6]})

with col22:
    st.write("1.b. Comparison of energy sources of the building (steam, electricity, natural gas) over the years")
    placeholder3 = st.empty()
    placeholder3.bar_chart({"data": [1, 5, 2, 6]})

##2nd chapter
st.subheader("2.Which characteristics of the building should be reviewed in terms of energy efficiency?")

#placeholder to be replaced with visuals  
st.write("2.a. Do <selected building's program> use more energy as compared to other program types?")              
placeholder4 = st.empty()
placeholder4.bar_chart({"data": [1, 5, 2, 6]})

st.write("2.b. Does the size of my building consume more energy in comparison?")
placeholder5 = st.empty()
placeholder5.bar_chart({"data": [1, 5, 2, 6]})


##3rd chapter
st.subheader("3.Are similar buildings in Seattle using same energy?")

col1, col2 = st.columns(2)

with col1:
    selectProgramFilter = st.selectbox("Select Program type",("Program Type","Office"))
    Year_range = st.slider('Year built',
                        min_value=int(1950),
                        max_value=int(2020)
                        )

    Area_range = st.slider('Area (sq.ft)',
                        min_value=int(10000),
                        max_value=int(202000)
                        )

    Floors_range = st.slider('Floors',
                        min_value=int(0),
                        max_value=int(60)
                        )

    EnergyStar_range = st.slider('EnergyStar',
                        min_value=int(0),
                        max_value=int(100)
                        )

    Zipcode_range = st.slider('Zipcode',
                        min_value=int(0),
                        max_value=int(100)
                        )

    Electricity_range = st.slider('Electricity Use',
                        min_value=int(0),
                        max_value=int(100)
                        )

    Gas_range = st.slider('Gas Use',
                        min_value=int(0),
                        max_value=int(100)
                        )


    GHG_range = st.slider('GHG emissions',
                        min_value=int(0),
                        max_value=int(100)
                        )


with col2:
    #placeholder to be replaced with visuals
    placeholder6 = st.empty()
    placeholder6.line_chart({"data": [1, 5, 2, 6]})



st.write("The building you have selected has a 380 EUI and energy star score of 54 in the comparison to a building with similar charecterists which has an EUI of 200 and the building standard of 150")