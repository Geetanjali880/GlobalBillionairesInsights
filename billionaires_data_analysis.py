#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd 
df = pd.read_csv("Billionaires Statistics Dataset.csv")
df.head()


# In[58]:


df.describe()


# In[59]:


df.isnull().sum()


# In[60]:


df.shape


# In[61]:


df = df.drop(["organization","title","state","residenceStateRegion"], axis=1)


# In[62]:


df


# In[63]:


numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(numerical_cols)


# In[64]:


categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(categorical_cols)


# In[65]:


print(df["birthDate"])


# In[66]:


df['birthDate'] = pd.to_datetime(df['birthDate'], errors='coerce')


# In[67]:


df['birthDate']


# In[68]:


df.columns


# In[69]:


print(df["birthYear"])


# In[70]:


df['gdp_country'] = df['gdp_country'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)



# In[71]:


import pandas as pd

# Ensure birthDate is datetime
df['birthDate'] = pd.to_datetime(df['birthDate'], errors='coerce')

# Today's date
today = pd.to_datetime('today')

# Calculate age
df['current_age'] = (
    today.year - df['birthDate'].dt.year
    - ((today.month < df['birthDate'].dt.month) |
       ((today.month == df['birthDate'].dt.month) & (today.day < df['birthDate'].dt.day)))
)


# In[72]:


df['current_age']


# In[73]:


df.isnull().sum()


# In[74]:


df.shape


# In[75]:


df[df.select_dtypes(include='int64').columns] = df.select_dtypes(include='int64').fillna(df.mean(numeric_only=True))


# In[76]:


df.isnull().sum()


# In[77]:


# Convert all int64 columns to float (can hold NaN + mean)
df[df.select_dtypes(include='int64').columns] = df.select_dtypes(include='int64').astype('float')


# In[78]:


df[df.select_dtypes(include='float').columns] = df.select_dtypes(include='float').fillna(df.mean(numeric_only=True))


# In[79]:


df.isnull().sum()


# In[83]:


for col in ['country', 'city']:
    mode_val = df[col].mode()[0]
    df[col].fillna(mode_val)


# In[84]:


df.isnull().sum()


# In[89]:


mode_date = df['birthDate'].mode()[0]
df['birthDate'].fillna(mode_date,inplace=True)


# In[90]:


df.isnull().sum()


# In[91]:


df = df[df['firstName'].notna()]


# In[92]:


df.isnull().sum()


# In[93]:


df.to_csv('cleaned_billionaires.csv', index=False)


# In[ ]:




