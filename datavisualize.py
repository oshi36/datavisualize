#!/usr/bin/env python
# coding: utf-8

# # Data Visualization on Weather Data 

# In[1]:


import pandas as pd
import seaborn as sns
sns.set(color_codes=True)


# In[2]:


weather = pd.read_csv('Test.csv')


# In[3]:


weather.head()


# In[4]:


weather.info()


# In[5]:


sns.barplot(weather['humidity'],weather['temperature'])


# In[6]:


sns.distplot(weather['humidity'])


# In[7]:


sns.jointplot(weather['humidity'],weather['temperature'])


# In[8]:


sns.jointplot(weather['humidity'],weather['temperature'], kind ="kde")


# In[10]:


sns.jointplot(weather['humidity'],weather['temperature'], kind ="hex")


# In[11]:


sns.pairplot(weather[['humidity' , 'temperature', 'air_pollution_index']])


# In[12]:


sns.stripplot(weather['weather_type'],weather['temperature'])


# In[13]:


sns.stripplot(weather['weather_type'],weather['temperature'], jitter =True)


# In[14]:


sns.swarmplot(weather['humidity'],weather['temperature'])


# In[15]:


sns.boxplot(weather['humidity'] ,weather['temperature'], hue=weather['weather_type'])


# In[16]:


sns.barplot(weather['humidity'] ,weather['temperature'], hue=weather['weather_type'])


# In[17]:


sns.countplot(weather['weather_type'])


# In[18]:


sns.pointplot(weather['humidity'] ,weather['temperature'], hue=weather['weather_type'])


# In[19]:


sns.lmplot(x="humidity" , y="temperature" ,data=weather)


# In[20]:


sns.lmplot(x="humidity" , y="temperature" ,hue="weather_type" ,data=weather)


# In[ ]:




