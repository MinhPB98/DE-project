#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
import numpy as np


# In[30]:


def drop_full_col(df): 
    ''' Drop full column if that column contains full NaN values'''
    # looping each column in dataframe
    for i in df.columns:
        # searching which columns contain FULL NaN value
        if df[i].isna().sum()==len(df): 
            # dropping those columns
            df.drop(i,axis=1,inplace=True) 
    return df


# In[31]:


def filling_NaN(df):
    ''' Filling the NaN value in columns if that column contains any NaN values'''
    # looping each column in dataframe
    for i in list(df.columns):
        # finding out which columns contain ANY NaN values
        if df[i].isna().sum() !=0 : 
            # printing out that column with how many NaN it has
            print(f'Number of NaN of {i} = {df[i].isna().sum()}')
            # replace that NaN value with 0 as default
            df[i] = df[i].replace(np.nan, 0)
    print("Filling successful")
    return df


# In[32]:


def remove_irrelevant_value(df, irr_value):
    '''Remove the irrelevant value in column '''
    # create blank list to contain which columns contain irrelevant value
    ls_col = [] 
    for col in list(df.columns):
        # if sum of irrelevant value contained in that column not equal to 0
        if df[col].apply(lambda x:x==irr_value).sum()!=0:  
            # append column to list
            ls_col.append(col) 
        else:
            pass
    for i in ls_col: 
        # drop these columns
        df = df[df[i] != irr_value] 
    return df

