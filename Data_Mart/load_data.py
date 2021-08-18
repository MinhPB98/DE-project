#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[3]:


def load_mean_data(dir_name):
    try:
        mean = '_Mart_Mean'
        path = '../Data_Mart/'+dir_name+mean+'/'
        name_csv = dir_name +'_mean_mart.csv'
        url = path + name_csv
        df = pd.read_csv(url)
        print("Loading mean file successfully")
        print(df) 
    except:
        print("\033[1;30;41m File does not exist !!! \n")


# In[ ]:


def load_sum_data(dir_name):
    try:
        mean = '_Mart_Sum'
        path = '../Data_Mart/'+dir_name+mean+'/'
        name_csv = dir_name +'_mean_mart.csv'
        url = path + name_csv
        df = pd.read_csv(url)
        print("Loading sum file successfully")
        print(df)
    except:
        print("\033[1;30;41m File does not exist !!! \n")

