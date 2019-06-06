#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


csv_path = "C:\\Users\\knm2m\\Desktop\\HW\\Python-challenge\\PyPoll\\03-Python_Homework_PyPoll_Resources_election_data.csv"


# In[6]:


Election_Data = pd.read_csv(csv_path)
Election_Data.head()


# In[5]:


print ("Election Results")


# In[8]:


total_votes = Election_Data['Voter ID'].nunique()
print(f"Total Voters: {total_votes}")


# In[9]:


candidate_table = Election_Data.groupby(["Candidate"])
candidate_group = pd.DataFrame(candidate_table['Voter ID'].agg(np.size))
candidate_group_sort = candidate_group.sort_values('Voter ID',ascending = False)


# In[10]:


total_votes1 = candidate_group_sort['Voter ID'].sum()
candidate_group_sort['Percentage']= candidate_group_sort['Voter ID']/total_votes1


# In[11]:


candidate_group_sort['Percentage'] = pd.Series(["{0:.3f}%".format(per * 100) for per in candidate_group_sort['Percentage']],index=candidate_group_sort.index)


# In[12]:


candidate_group_sort["string_Voter_ID"]="("+candidate_group_sort['Voter ID'].astype(str) + ")"


# In[13]:


candidate_group_sort['Candidate1']=candidate_group_sort.index


# In[14]:


candidate_group_sort_display = candidate_group_sort[['Percentage','string_Voter_ID']]
candidate_group_sort_display.columns = ["",""]
del candidate_group_sort_display.index.name
print(candidate_group_sort_display)


# In[15]:


winner = candidate_group_sort.iloc[0,3]


# In[16]:


print()
print(f"Winner: {winner}")


# In[ ]:




