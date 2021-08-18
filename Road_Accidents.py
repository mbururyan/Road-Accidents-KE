#!/usr/bin/env python
# coding: utf-8

# # Loading the Libraries onto the notebook

# In[1]:

# Importing Streamlit
import streamlit as st


# Pandas and numpy

import pandas as pd
import numpy as np


# ## Loading the datasets onto the notbook

# In[2]:

#Dattaframe name
st.write('Distpay first dataframe')

# Loading first dataset
def load_data(type, path):
  if type == 'csv':
    car = pd.read_csv(path)
  return car

df = load_data('csv', 'Car_Insurance_Claim copy.csv')

df.head()
st.write(df.head())
st.dataframe(df)

# In[3]:


# Loading second dataset
df_victims = load_data('csv', 't0003-10.1080_23311916.2020.1797981.csv')

df_victims.head()


# ## Information on the datasets

# In[4]:


# function to display info of a dataframe
def info(dataframe):
    return dataframe.info()


# In[5]:


# First dataset's information
info(df)


# In[6]:


# Second dataset's info
info(df_victims)


# # Data Preparation

# # Data Cleaning

# ### Operations to de done on the dataset when cleaning
# 
# #### First Dataset
# 
# 1. Dropping 'Outcome' Column from the first dataset
# 2. Handling null values :
# - In the credit scores, null values will be handled by replacing the null value with 0
# - In the annual mileage column, null values will be replaced by fowardfill method
# 3. Check for duplicates and drop from the dataset if any
# 4. Change datatypes for Married and Children column to boolean
# 
# #### Second Dataset
# 1. Dropping unwanted columns : 'NATIONAL TRANSPORT AND SAFETY AUTHORITY' and unnamed6
# 2. Dropping unwanted rows
# 3. Change column names
# 4. Changing datatypes. Object and Cause Code columns to integer.

# 

# In[7]:


# First Dataset

# Dropping 'Outcome' column

df.drop(['OUTCOME'], axis=1, inplace=True)
df.head()


# In[8]:


# Handling null values

# Credit scores columns, replace 0 with null

df['CREDIT_SCORE'].fillna(0, inplace=True)
df.head()


# In[9]:


# Replace null value for Annual Mileage by foward fill

df['ANNUAL_MILEAGE'].fillna(method='ffill', inplace=True)
df.head()


# In[10]:


# check for duplicates
df.duplicated().sum()


# No duplicates were found in the dataset
# 

# In[11]:


# Change datatype of Married column to boolean

df['MARRIED'] = df['MARRIED'].astype(bool)
df.head()


# In[12]:


# Change values in Children to boolean type
df['CHILDREN'] = df['CHILDREN'].astype(bool)
df['VEHICLE_OWNERSHIP'] = df['VEHICLE_OWNERSHIP'].astype(bool)
info(df)


# #### Cleaning second dataset

# In[13]:


# Dropping columns
df_victims.drop(['NATIONAL TRANSPORT AND SAFETY AUTHORITY'], inplace=True, axis=1)


# In[14]:


# Drop first 8 rows
df_victims_sliced = df_victims[10:]

df_victims_sliced.columns=['S/N', 'NAME OF VICTIM', 'GENDER', 'AGE', 'CAUSE CODE', 'VICTIM', 'NUMBER']


# In[15]:


df_victims_sliced.info()


# In[16]:


#changing datatypes
df_victims_sliced[['AGE', 'CAUSE CODE', 'NUMBER']] = df_victims_sliced[['AGE', 'CAUSE CODE', 'NUMBER']].astype(int)
# replacing ' ' with '_'
df_victims_sliced.columns = df_victims_sliced.columns.str.replace(' ', '_')
info(df_victims_sliced)


# ### Print out cleaned Dataframes

# In[17]:


df.head()


# In[18]:


df_victims_sliced


# In[19]:


#Exporting to new clean datasets

df_clean = df.to_csv('cleaned_road_accidents.csv')
df_clean


# In[20]:


df_victims_clean = df_victims_sliced.to_csv('cleaned_road_victims.csv')
df_victims_clean


# # Analysis
# 

# In[21]:


# Loading cleaned dataset
df = pd.read_csv('cleaned_road_accidents.csv')
df.head()


# ## Functions

# In[22]:

st.write('Analysis :')
# Grouping by sum function 
# column - column to aggregate
# grouper - column to groupby
def grouper(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.sum().sort_values(ascending=False)


# In[23]:


# Grouping function by mean
# column - column to aggregate
# grouper - column to groupby
def groupermean(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.mean().sort_values(ascending=False)


# In[24]:


# Grouping function by count
# column - column to aggregate
# grouper - column to groupby
def groupercount(column, grouper):
    group = df[column].groupby(df[grouper])
    return group.count().sort_values(ascending=False)


# In[25]:


# Grouping function by count advanced
def grouper2(name, condtion, grouping):
    name = df[(df['INCOME'] == condtion)]
    group = name.groupby(name[grouping])
    return group[grouping].count().sort_values(ascending=False)


# ## Answering the Primary objective

# ### Determining which age group of drivers were most involved in:
# 1. Road accidents
# 2. Speeding violations
# 3. Caught driving under the influence.
# 

# In[26]:


# Which age group was most invilved in road accidents
age_accident = grouper('PAST_ACCIDENTS', 'AGE')
age_accident


# The age group mostly involved in road accidents is drivers in the range of 40-64 yrs.

# In[27]:


# Which age group was most involved in speeding violations
age_speed = grouper('SPEEDING_VIOLATIONS','AGE')
age_speed


# The age group of 65+ are mostly inolved in speeding violations

# In[28]:


# Which agegroup was caught the most times driving under the influence
age_drunk = grouper('DUIS', 'AGE')
age_drunk


# The age group in the range 40-64 are mostly involved in DUIS

# # Other Objectives

# ## Gender most involved in road accidents in Kenya.

# In[29]:


# Which gender is most involved in road accidents in Kenya.
gender_accident = grouper('PAST_ACCIDENTS', 'GENDER')
gender_accident


# Males are mostly involved in road accidents with a sum of 7115

# ## Are more experienced or less experienced Drivers more likely to be caught in accidents and overspeeding?

# In[30]:


# Determining whether more or less experienced drivers are more likely to be caught in accidents.
exp_accident = grouper('PAST_ACCIDENTS','DRIVING_EXPERIENCE')
exp_accident


# Drivers with a driving experience between 20-29y are mostly involved in accidents

# Drivers with a driving experience between 0-9y are least involved in accidents

# In[31]:


# Determining whether more or less experienced drivers are more likely to be caught overspeeding.
exp_speed = grouper('SPEEDING_VIOLATIONS','DRIVING_EXPERIENCE')
exp_speed


# Drivers with a driving experience between 20-29y are mostly involved in speeding violations

# Drivers with a driving experience between 0-9y are least involved in accidents

# ## Type of vehicle involved in accidents & Over-speeding the most often

# In[32]:


# What type of vehicle is most involved in road accidents 
vehicle_accident = grouper('PAST_ACCIDENTS','VEHICLE_TYPE')
vehicle_accident


# The sedan type of car are mostly involved in road accidents

# In[33]:


# What type of vehicle is most involved in speeding violations
vehicle_speed = grouper('SPEEDING_VIOLATIONS','VEHICLE_TYPE')
vehicle_speed


# The sedan type of car are mostly involved in speeding violations

# ## Accidents are caused the most often by drivers of what educational background?

# In[34]:


# Drivers most involved in accidents are of what educational background?
education_accident = grouper('PAST_ACCIDENTS','EDUCATION')
education_accident


# University graduates are mostly involved in car accidents

# In[35]:


# Drivers with the most speeding violations are of what educational background?
education_speed = grouper('SPEEDING_VIOLATIONS','EDUCATION')
education_speed


# University graduates are mostly involved in speeding violation

# ## When causing accidents or everspeeding, do most of the drivers own the vehicle?

# In[36]:


# Determining whether most of the motorists involved in accidents own the vehicle or not.
owner_accident = grouper('PAST_ACCIDENTS','VEHICLE_OWNERSHIP')
owner_accident


# Drivers owning vehicles are mostly involved in road accidents

# In[37]:


# Determining whether most of the drtivers with speeding violations own the vehicle or not.
owner_speed = grouper('SPEEDING_VIOLATIONS','VEHICLE_OWNERSHIP')
owner_speed


# Drivers owning vehicles are mostly involved in speed violations

# ## Did more accidents happen in Kenya before 2015 or after 2015

# In[38]:


# Did most accidents occur before 2015 or after?
year_accident = grouper('PAST_ACCIDENTS','VEHICLE_YEAR')
year_accident


# Most road accidents in Kenya happened before 2015

# ## What economic class of Kenyans are the most involved in road accidents?

# In[39]:


# Determining which class of Kenyans is the most involved in road accidents in Kenya.
class_accident = grouper('PAST_ACCIDENTS','INCOME')
class_accident


# The upper class are mostly involved in road accidents

# ## Which economic class of Kenyans cover the most distance annually when driving?

# In[40]:


# Which class of Kenyans covers the most distance/mileage on average?
class_distance = groupermean('ANNUAL_MILEAGE','INCOME')
class_distance


# Kenyans in poverty covered the most distance when driving

# ## What type of vehicle is most owned by single drivers and married drivers?

# In[41]:


# Which type of vehicle is most owned by single motorists
single = df[(df['MARRIED'] == False)]
group = single.groupby('VEHICLE_TYPE')
single_vehicle = group['VEHICLE_TYPE'].count()
single_vehicle


# The most owned vehicles for single motorists is sedan

# In[42]:


# Which type of vehicle is most owned by married motorists
single = df[(df['MARRIED'] == True)]
group = single.groupby('VEHICLE_TYPE')
married_vehicle = group['VEHICLE_TYPE'].count()
married_vehicle


# The most owned vehicles for married  motorists is sedan

# ## Type of victim most affected by road accidents in Kenya

# In[43]:


# Type of victim most affected by road accidents
group = df_victims_sliced['NUMBER'].groupby(df_victims_sliced['VICTIM'])
victim_accident = group.count().sort_values(ascending=False)
victim_accident


# Pedestrians are the most killed victims by road accidents

# # Analysis Questions

# ## Average credit scores for different economic classes of Kenyan Drivers

# In[44]:


# The average credit score for different classes of Kenyan drivers
class_credit = groupermean('CREDIT_SCORE','INCOME')
class_credit


# These are average of each Income class in the dataset

# ## Kenyan drivers in the upper class, working-class, and poverty income category are mainly from what educational background

# In[45]:


# Kenyans in the upper class, working-class, and poverty income category are 
# mainly from what educational background

# Determinig the Income classes present in the dataset
list(df['INCOME'].unique())


# In[46]:


# Creating new dataset based on the income class
upperclass = df[(df['INCOME'] == 'upper class')]
working_class = df[(df['INCOME'] == 'working class')]
poverty = df[(df['INCOME'] == 'poverty')]


# In[47]:


# For upperclass
class_upper = grouper2('upper class', 'upper class', 'EDUCATION')
class_upper


# In the upper class the mostly involved are the university graduates

# In[48]:


# For working class
class_working = grouper2('working_class', 'working class', 'EDUCATION')
class_working


# Working class drivers are mainly highschool grads

# In[49]:


# For middle class 
middle_class = df[(df['INCOME'] == 'middle class')]
grouper2('middle_class', 'middle class', 'EDUCATION')


# In the middle class the mostly involved are the high school graduates

# In[50]:


# For poverty class
class_poor = grouper2('poverty', 'poverty', 'EDUCATION')
class_poor


# In the poverty class personels with no education are mostly involved in road accidents

# ## Which class of Kenyans covers the most and least distance when driving?

# In[51]:


# Which class of Kenyans covers the most and least distance when driving?
class_distance = groupermean('ANNUAL_MILEAGE','INCOME')
class_distance


# ### Kenyans in poverty cover the most distance annually when driving

# ## The average credit score of Kenyan Drivers

# In[52]:


# What are the average credit scores of Kenyan drivers?
credit_mean = df['CREDIT_SCORE'].mean()
credit_mean


# The average credit score for kenyan drivers is: 0.46515999169979966

# ## Total number of accidents and speeding violations that happened on Kenyan roads

# In[53]:


# How many accidents and speeding violations happened in total in KE?

# Sum of PAST_ACCIDENTS accidents
total_accidents = df['PAST_ACCIDENTS'].sum()
total_accidents


# The total number of accidents in Kenya is 10563

# In[54]:


# Sum of SPEEDING_VIOLATIONS
total_speed = df['SPEEDING_VIOLATIONS'].sum()
total_speed


# The total number of speeding violations in KE is 14829

# # Data Visualization
# 

# In[55]:

st.write('Data Visualization :')
#Importing plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns

# More libraries
# import graphviz as graphviz
# ## Age groups of Drivers involved in accidents, speeding violations and DUIS

# In[ ]:


# Age group of drivers most involved in accidents
age_accident.plot(kind='bar')

st.bar_chart(data=age_accident)


# In[ ]:


# Age group of drivers with the most speeding violations
age_speed.plot(kind='bar')

st.bar_chart(data=age_speed)

# In[ ]:


# Age group of drivers most caught driving under the influence
age_drunk.plot(kind='bar')

st.line_chart(data=age_drunk)

# ## The gender of drivers involved in car accidents
# 

# In[ ]:


# Gender most involved in car accidents
gender_accident.plot(kind='pie')

st.area_chart(data=gender_accident)

# ## Driving experience

# In[ ]:


# Drivers of what experience of driving are most involved in road accidents
exp_accident.plot(kind='barh')

st.bar_chart(data=exp_accident)
# In[ ]:


# Drivers of what experience get the most speeding tickets
exp_speed.plot(kind='barh')
exp_speed

st.bar_chart(data=exp_speed)

# ## Type of vehicle that is the most involved in car accidents and over speeding

# In[ ]:


#Type of vehicle involved in most accidents
vehicle_accident.plot(kind='bar')

st.bar_chart(data=vehicle_accident)
# In[ ]:


#Vehicles involved in the most issuing of speeding tickets
vehicle_speed.plot.bar()

st.bar_chart(data=vehicle_speed)
# ## Educational background of drivers involved in accidents and over-speeding

# In[ ]:


education_accident.plot(kind='bar')

st.line_chart(data=education_accident)
# In[ ]:


education_speed.plot.bar(alpha=0.5)

st.line_chart(data=education_speed)

# ## Are most of the vehicles in accidents and speeding violations personally owned by the culprit?

# In[ ]:


owner_accident.plot.pie()


# In[ ]:


owner_speed.plot.pie()


# ## If most accidents occured before or after 2015

# In[ ]:


year_accident.plot.pie(colors=['b','g'])


# ## Financial class of kenyans per accidents caused, distance covered annually and their average credit score 

# In[ ]:


class_accident.plot.bar()

st.bar_chart(data=class_accident)
# In[ ]:


class_distance.plot.line()

st.line_chart(data=class_distance)

# In[ ]:


class_credit.plot.barh()

st.line_chart(data=class_credit)
# ## Vehicles most driven by single drivers vs married drivers

# In[ ]:


single_vehicle.plot.barh()




# In[ ]:


married_vehicle.plot.barh()


# ## Victims involved in the most accidents

# In[ ]:


victim_accident.plot.pie()

