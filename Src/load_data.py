#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


def load_data(file_name,df):
    df.to_csv('../Data_Warehouse/'+file_name+'_cleaned.csv',index=False)
    return "Loading data into Warehouse successful"

