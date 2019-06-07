#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


csv_path = "C:\\Users\\knm2m\\Desktop\\HW\\Python-challenge\\PyBank\\03-Python_Homework_PyBank_Resources_budget_data.csv"
df = pd.read_csv(csv_path)
df.head()


# In[10]:


#number of months = "Date"
df.count(axis = 0) 


# In[11]:


Total = df['Profit/Losses'].sum()
print (Total)


# In[15]:


df.pct_change("Profit/Losses")


# In[ ]:




