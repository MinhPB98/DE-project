#!/usr/bin/env python
# coding: utf-8

# In[12]:


from utils import drop_full_col, filling_NaN,remove_irrelevant_value


# In[33]:


def clean_data(df,keyword):
    drop_full_col(df)
    df = remove_irrelevant_value(df,keyword)
    filling_NaN(df)
    return df

