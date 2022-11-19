#############################################################################
# This project is ///
# Course: Interactive Data Science(05839-A)
# Coded By: Jeffrey Na, Ninad Bandewar
# AndrewID: jjna, nbandewa
# Date: Oct 09, 2022
# Thanks to Prof. John Stamper, Prof. Adam Perer & TAs for there assistance
#############################################################################

#############################################################################
# Library Imports
#############################################################################
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data

#############################################################################
# Data Import
#############################################################################
st.set_page_config(layout = "wide")

@st.cache
def load(url):
    return pd.read_csv(url, encoding = "latin1")

df = load("https://raw.githubusercontent.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/main/Combined.csv")

if st.checkbox("Show Raw Data"):
    st.write(df)