#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("../Project Anomaly Price Hikes Detection/Anomalies/Anomaly 19.csv", nrows=1000000)


# In[3]:


columns = [i for i in data.columns]


# In[4]:


columns


# In[7]:


data['knumh'] = data['knumh'].replace(',','')
data['knumh'] = pd.to_numeric(data['knumh'])


# In[8]:


data['kbetr'] = data['kbetr'].str.replace(',','')
data['kbetr'] = pd.to_numeric(data['kbetr'])


# In[9]:


data['kpein'] = data['kpein'].str.replace(',','')
data['kpein'] = pd.to_numeric(data['kpein'])


# In[11]:


plt.stem(data['knumh'], data['kbetr'], use_line_collection=True)


# In[12]:


plt.show()


# In[ ]:




