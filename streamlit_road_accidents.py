# Importing Streamlit
import streamlit as st


# Pandas and numpy

import pandas as pd
import numpy as np

import time

# First Dataset

st.write('GROUP 6 PROJECT')

st.write('First Dataset')

def load_data(type, path):
  if type == 'csv':
    car = pd.read_csv(path)
  return car

df = load_data('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_accidents.csv')

df_victims = load_data('csv', '/Users/RyanMburu/Documents/DS Projects/Prep/Road_Accidents_1/cleaned_road_victims.csv')
df.head()

st.write('First DataFrame')

st.dataframe(df)
st.dataframe(df_victims)

# First widget

x = st.slider('x')
st.write(x, 'squared is', x*x)

# Layout
selectbox1 = st.sidebar.selectbox('How would you like your stake?', ('raw', 'medium', 'roasted'))

st.write('you selected:', selectbox1)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('First Map!')

map_data = pd.DataFrame(np.random.randn(1000,2) / [5, 5] + [37, -122], columns=['lat', 'lon'])

st.map(map_data)

# Progress bar

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
# Update the progress bar with each iteration. 
 latest_iteration.text(f'Iteration {i+1}') 
 bar.progress(i + 1)
 time.sleep(0.1)
