#!/usr/bin/env python
# coding: utf-8

# # Importing the libraries.
# 1.numpy and pandas for manupilation<br>
# 2.matplotlib and for visualization<br>

# In[102]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# # Lets read the Dataset

# In[12]:


data = pd.read_excel('Navi.xlsx')


# In[18]:


print("shap of the dataset :", data.shape)


# # We have total 32293 installations

# In[16]:


data.head()


# # Checking the null spaces

# In[17]:


data.isnull().sum()


# In[22]:


missing_data = data.isnull()
missing_data.head(5)


# "True" means the value is a missing value while "False" means the value is not a missing value.

# # <h4>Calculate the mean value for the "Postback Http Response Code" column </h4>

# In[63]:


avg_Postback_Http = data["Postback Http Response Code"].astype('float64').mean(axis=0)
print("Postback Http Response Code:", avg_norm_loss)


# <h4>Replace "NaN" with mean value in "Postback Http Response Code" column</h4> 

# In[77]:


data["Postback Http Response Code"].replace(np.nan, avg_Postback_Http, inplace=True)


# #  Clicks on a particular time

# In[78]:


data['Attributed Touch Time'].value_counts()


# In[115]:


data['Device Type'].value_counts()


# In[108]:


data['Attributed Touch Time'].value_counts()[:20].plot(kind='barh')
plt.title("Number of clicks on particular time")


# # How many installs on particular time

# In[111]:


data['Install Time'].value_counts()[:20].plot(kind='barh')
plt.title("Number of installs on particular time")


# # We have maximum installations on 27th of May 2021

# In[101]:


data['State'].value_counts()[0:20].plot(kind='barh')


# # We have maximum installations from MH(Maharastra)

# In[110]:


data['City'].value_counts()[0:20].plot(kind='barh')


# # 1.From cities we have most from Delhi 
# # 2.From Maharastra we have most from Mumbai

# In[113]:


data['Operator'].value_counts()[0:20].plot(kind='barh')


# # Most of the installation operator are Jio 4G

# In[114]:


data['Device Type'].value_counts()[0:20].plot(kind='barh')


# # Micromax C1 phone is at top with 750, Bouble and Truple than most of the phones

# In[120]:



data['Platform'].value_counts()[0:20].plot(kind='hist')


# # All the phones are Android

# In[121]:


data['App Version'].value_counts()[0:20].plot(kind='barh')


# # Most of the app versions are 1.3.7, 1.5.9, 1.6.0

# In[ ]:





# In[ ]:




