# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Containers
home = st.container()
analysis = st.container()

# Home
with home:
    #Introduction
    st.title('GROUP 6 PROJECT')
    st.write(''' 
    ## ROAD ACCIDENTS IN KE
    This is a group project that aims at gathering insights that happens on Kenyan roads such as the age groups most involved in accidents and overspeeding
    and the type of victim most affected, among other analysis to be covered.

    This project aims at providing as much insights as possible so as to ensure road accidents reduce as a whole in our nation.
    ''')

    # Loading in the datasets
    def load_dataframe(type, path):
        if type == 'csv':
            new_data = pd.read_csv(path)
        return new_data

    df = load_dataframe('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_accidents.csv')

    #promt checkbox for displaying dataframe
    if st.checkbox('Display Road Accidents Data Frame?'):
        st.subheader('Road Accidents in KE')
        st.dataframe(df)

    # More information on the Project
    st.write('''
    The project allows you, the user to pick whichever characteristics of Kenyan drivers and see if there is any corelations with accidents caused, number of speeding violations they
    are caught in and how many times they are caught driving under the influence of alcohol.
    Such characteristics include :

    1. Age of the Drivers

    2. Gender

    3. Financial Background

    4. Educational Background

    5. The driver's experience etc.
    ''')

with analysis:
    st.sidebar.subheader('Pick a characteristic of your liking :')
    analysis_questions = st.sidebar.selectbox('Driver Characteristic', 
    options = [
        '---',
        'Age group of the drivers',
        'Gender',
        'Race',
        'Driving Experience',
        'Education level',
        'Social class',
        'Vehicle ownership status',
        'Type of vehicle'], index=0)

    # Analysis functions
    def grouper(column, grouper):
        group = df[column].groupby(df[grouper])
        return group.sum().sort_values(ascending=False)

    def groupermean(column, grouper):
        group = df[column].groupby(df[grouper])
        return group.mean().sort_values(ascending=False)

    def groupercount(column, grouper):
        group = df[column].groupby(df[grouper])
        return group.count().sort_values(ascending=False)
    
    def grouper2(name, condtion, grouping):
        name = df[(df['INCOME'] == condtion)]
        group = name.groupby(name[grouping])
        return group[grouping].count().sort_values(ascending=False)

    # call the datasets again
    df = load_dataframe('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_accidents.csv')

    #Age group
    if analysis_questions == 'Age group of the drivers':
        st.subheader('AGE GROUP OF KENYANS WHO CAUSED MOST ACCIDENTS')
        age_accident = grouper('PAST_ACCIDENTS', 'AGE')
        st.bar_chart(age_accident)
        if st.checkbox('Show Raw Data?'):
            st.table(age_accident)

        st.subheader('AGE GROUP OF KENYANS WHO HAD MOST SPEEDING VIOLATIONS')
        age_speed = grouper('SPEEDING_VIOLATIONS', 'AGE')
        st.bar_chart(age_speed)
        if st.checkbox('Show Raw data?'):
            st.table(age_speed)

        st.subheader('AGE GROUP CAUGHT DRIVING UNDER THE INFLUENCE THE MOST OFTEN')
        age_drunk = grouper('DUIS', 'AGE')
        st.bar_chart(age_drunk)

    # Gender
    elif analysis_questions == 'Gender':
        st.subheader('GENDER INVOLVED IN MOST ACCIDENTS')
        gender_accident = grouper('PAST_ACCIDENTS', 'GENDER')
        st.table(gender_accident)

