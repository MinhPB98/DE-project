#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd 
import os
from ingest_warehouse import ingest_dwh


# In[43]:


def create_mart_mean(dir_name,df):
    # dir_name = input("Input mart: ")

    # Parent Directories 
    try:
        parent_dir = "../Data_Mart/"
        mean = '_Mart_Mean'
        # Path 
        path = os.path.join(parent_dir, dir_name+mean) 
        dir_full = dir_name + mean
        os.makedirs(path)
        print(f"Directory {dir_full} created") 
        for i in list(df.columns):
            if i == dir_name:
                data = df.groupby([i],as_index=False).mean()
        path = '../Data_Mart/'+dir_name+mean+'/'
        name_csv = dir_name +'_mean_mart.csv'
        data.to_csv(path+name_csv ,index=False)
        print(f"{name_csv} created !!!")
    except:
        print("\033[1;30;41m File has existed !!! \n")


# In[44]:


def create_mart_sum(dir_name,df):
    # dir_name = input("Input mart: ")

    # Parent Directories 
    try:
        parent_dir = "../Data_Mart/"
        mean = '_Mart_Sum'
        # Path 
        path = os.path.join(parent_dir, dir_name+mean) 
        dir_full = dir_name + mean
        os.makedirs(path)
        print(f"Directory {dir_full} created") 
        for i in list(df.columns):
            if i == dir_name:
                data = df.groupby([i],as_index=False).sum()
        path = '../Data_Mart/'+dir_name+mean+'/'
        name_csv = dir_name +'_mean_mart.csv'
        data.to_csv(path + name_csv,index=False)
        print(f"{name_csv} created !!!")
    except:
        print("\033[1;30;41m File has existed !!! \n")


# In[ ]:




