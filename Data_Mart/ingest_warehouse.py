#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


def ingest_dwh(file_name):
    try:
        file_name = file_name +'_cleaned.csv'
        url = '../Data_Warehouse/'+file_name
        df = pd.read_csv(url)
        print("Your data is ingested succesfully")
        return df
    except:
        print(f"\033[1;31;47m {file_name} is not available. Check your data source \n")

