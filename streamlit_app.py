import streamlit as st
import pandas as pd
import numpy as np

## Data viz imports

import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("California Housing - Real Estate Agency")
df = pd.read_csv("housing.csv")
page = st.sidebar.selectbox("Select Page",["Introduction","Data Viz"])


if page == "Introduction":

    st.subheader("01 Introduction")

    st.markdown("##### Data Preview")

    rows = st.slider("Select a number of rows",5,20,5)
    
    st.dataframe(df.head(rows))

    st.markdown("##### Missing Values")

    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum()==0:
        st.success("No missing values found")
    else:
        st.warning("You have some missing values")

    st.markdown("#### Statistical Summary")

    if st.button("Generate Statistical Summary"):
        st.dataframe(df.describe())

elif page == "Data Viz":

    col_x = st.selectbox("Select X axis variable",df.columns,index=0)
    col_y = st.selectbox("Select Y axis variable",df.columns,index=1)

    st.subheader("Bar Chart")
    st.bar_chart(df[[col_x,col_y]])


    st.subheader("Line Chart")
    st.line_chart(df[[col_x,col_y]])