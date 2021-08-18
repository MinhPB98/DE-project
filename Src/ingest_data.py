#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 


# ## Read data from github

# **CSV File**

# In[1]:


def Extract_data(file_name):
    try:
        file_name = file_name +'.csv'
        url = 'https://github.com/MinhPB98/Data-source/blob/master/Data_Source/'+file_name+'?raw=True'
        df = pd.read_csv(url,error_bad_lines=False)
        df.to_csv('../Data_Lake/'+file_name,index=False) # save to data lake 
        print("Your data is loaded succesfully in Data Lake")
        return df
    except:
        print(f"\033[1;31;47m {file_name} is not available. Check your data source \n")


# **Json File**

# In[8]:


def ingest_json_from_github(file_name):
    try:
        file_name = file_name +'.json'
        url = 'https://github.com/MinhPB98/Data-source/blob/master/Data_Source/'+file_name+'?raw=True'
        df = pd.read_json(url,lines=True)
        df.to_json('../Data_Lake/'+file_name)
        return "Your data is loaded succesfully in Data Lake"
    except:
        print(f"\033[1;31;47m {file_name} is not available. Check your data source \n")


# ## Reading CSV file

# In[ ]:


def read_csv_from_lake(file_name):
    ''' Read csv file from data lake '''
    try:
        # reading file from data lake folder
        df = pd.read_csv('../Data_Lake/' + file_name+'.csv')
        print("File is read successful")
        # return dataframe
        return df
    except:
        print("\033[1;31;47m There is no file. Please try again!!! \n")

