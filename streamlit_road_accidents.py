# Importing Streamlit
import streamlit as st


# Pandas and numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# First Dataset

st.title('GROUP 6 PROJECT')

st.write('''
## ROAD ACCIDENTS IN KE
This is a group project that aims at gathering insights that happens on Kenyan roads such as the age groups most involved in accidents and overspeeding
and the type of victim most affected, among other analysis to be covered.

This project aims at providing as much insights as possible so as to ensure road accidents reduce as a whole in our nation.

''')



# st.write('First Dataset')
st.subheader('Projects datasets')
def load_data(type, path):
  if type == 'csv':
    car = pd.read_csv(path)
  return car

df = load_data('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_accidents.csv')

df_victims = load_data('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_victims.csv')
df.head()

# st.write('First DataFrame')
#Checkbox to ask if user wants to see the datasets
if st.checkbox('Show Road Accidents Dataset?'):
    st.subheader('Road Accidents in Kenya')
    st.dataframe(df)

if st.checkbox('Show Victims Dataset?'):
    st.subheader('Analysis data of Age groups per accidents caused')
    st.dataframe(df_victims)



# st.dataframe(df)
# st.dataframe(df_victims)

# First slider

# x = st.slider('x')
# st.write(x, 'squared is', x*x)

# Layout
# selectbox1 = st.sidebar.selectbox('How would you like your stake?', ('raw', 'medium', 'roasted'))

# st.write('you selected:', selectbox1)

# add_slider = st.sidebar.slider(
    # 'Select a range of values',
    # 0.0, 100.0, (25.0, 75.0)
# )
# st.write('First Map!')

# map_data = pd.DataFrame(np.random.randn(1000,2) / [5, 5] + [37, -122], columns=['lat', 'lon'])

# st.map(map_data)

# Progress bar

latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
# Update the progress bar with each iteration. 
 #latest_iteration.text(f'Iteration {i+1}') 
 #bar.progress(i + 1)
 #time.sleep(0.1)


# Loading all the analysis functions

# Grouping by sum function 
# column - column to aggregate
# grouper - column to groupby
def grouper(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.sum().sort_values(ascending=False)

# Grouping function by mean
# column - column to aggregate
# grouper - column to groupby
def groupermean(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.mean().sort_values(ascending=False)

# Grouping function by count
# column - column to aggregate
# grouper - column to groupby
def groupercount(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.count().sort_values(ascending=False)

# Grouping function by count advanced
def grouper2(name, condtion, grouping):
    name = df[(df['INCOME'] == condtion)]
    group = name.groupby(name[grouping])
    return group[grouping].count().sort_values(ascending=False)


# Plotting function
def plotter(df_name, kind):
    df_name.plot(kind=kind)

# Checkbox function
def check_box(analysis_table):
    if st.checkbox('Show raw data:') == True:
        st.table(analysis_table)

# Age group with most accidents
st.subheader('AGE GROUP WITH MOST ACCIDENTS IN KE')
age_accident = grouper('PAST_ACCIDENTS', 'AGE')

# Bar graph
st.bar_chart(age_accident)

#Checkbox to ask if user wants to see the raw data
check_box(age_accident)

# Age group with most aspeeding violations
st.subheader('AGE GROUP WITH MOST SPEEDING VIOLATIONS IN KE')
age_speed = grouper('SPEEDING_VIOLATIONS', 'AGE')

# Bar graph
st.bar_chart(age_speed)

# Age group with most DUIS
st.subheader('AGE GROUP CAUGHT DRIVING UNDER THE INFLUENCE THE MOST')
age_duis = grouper('DUIS', 'AGE')
st.bar_chart(age_duis)

#class of kenyans involved in most accidents
st.subheader('CLASSES OF KENYANS INVOLVED IN MOST ACCIDENTS')
class_accidents = grouper('PAST_ACCIDENTS', 'INCOME')
st.table(class_accidents)

# Type of vehicle with most accidents
st.subheader('VEHICLE INVOLVED IN MOST ACCIDENTS')
vehicle_accident = grouper('PAST_ACCIDENTS', 'VEHICLE_TYPE')
st.bar_chart(vehicle_accident)

# AVG Credit scores
st.subheader('AVERAGE CREDIT SCORES OF KENYAN DRIVERS')
credit_class = groupermean('CREDIT_SCORE', 'INCOME')
st.line_chart(credit_class)

st.sidebar.subheader('DRIVER DETAILS')
# list of ages
list_ages = list(df['AGE'].drop_duplicates())


uploaded_df = st.sidebar.file_uploader('Upload CSV', type=['csv'])

# Define sidebar and its content
def user_input_features():
    age = st.sidebar.multiselect('AGE:', list_ages, default=list_ages)
    gender = st.sidebar.selectbox('GENDER : ', ('male', 'female'))
    race = st.sidebar.selectbox('RACE : ', ('majority', 'minority'))
    driving_experience = st.sidebar.selectbox('DRIVING EXPERIENCE : ', ('0-9y', '10-19y', '20-29y', '30+'))
    education = st.sidebar.selectbox('EDUCATION LEVEL : ', ('none', 'highschool', 'university'))
    income = st.sidebar.selectbox('INCOME : ', ('poverty', 'working class', 'middle class', 'upper class'))
    credit_score = st.sidebar.slider('CREDIT SCORE', 0.0, 0.9, 0.0)
    vehicle_ownership = st.sidebar.selectbox('VEHICLE OWNERSHIP : ', ('TRUE', 'FALSE'))
    car_type = st.sidebar.selectbox('CAR TYPE : ', ('sedan', 'sports car'))

    gender_data = df[df['GENDER'] == gender]
    # age_data = df[df['AGE'] == age]


    data = { 'AGE' : [age], 
    'GENDER' : [gender],
    'RACE' : [race],
    'DRIVING_EXPERIENCE' : [driving_experience],
    'EDUCATION ' : [education],
    'INCOME ' : [income],
    'CREDIT_SCORE' : [credit_score],
    'CAR TYPE' : [car_type]
    
    }
    features = pd.DataFrame(data)
    return features

df_user_input = user_input_features()

st.dataframe(df_user_input)


    
