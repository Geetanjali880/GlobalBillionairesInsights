#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df = pd.read_csv("Billionaires Statistics Dataset.csv")
df.head()


# In[2]:


df.describe()


# In[3]:


df.isnull().sum()


# In[4]:


df.shape


# In[5]:


df = df.drop(["organization","title","state","residenceStateRegion"], axis=1)


# In[6]:


df


# In[7]:


numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(numerical_cols)


# In[8]:


categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(categorical_cols)


# In[9]:


print(df["birthDate"])


# In[10]:


df['birthDate'] = pd.to_datetime(df['birthDate'], errors='coerce')


# In[11]:


df['birthDate']


# In[12]:


df.columns


# In[13]:


print(df["birthYear"])


# In[14]:


df['gdp_country'] = df['gdp_country'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)



# In[15]:


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


# In[16]:


df['current_age']


# In[17]:


df.isnull().sum()


# In[18]:


df.shape


# In[19]:


df[df.select_dtypes(include='int64').columns] = df.select_dtypes(include='int64').fillna(df.mean(numeric_only=True))


# In[20]:


df.isnull().sum()


# In[21]:


# Convert all int64 columns to float (can hold NaN + mean)
df[df.select_dtypes(include='int64').columns] = df.select_dtypes(include='int64').astype('float')


# In[22]:


df[df.select_dtypes(include='float').columns] = df.select_dtypes(include='float').fillna(df.mean(numeric_only=True))


# In[23]:


df.isnull().sum()


# In[24]:


for col in ['country', 'city']:
    mode_val = df[col].mode()[0]
    df[col].fillna(mode_val)


# In[25]:


df.isnull().sum()


# In[26]:


mode_date = df['birthDate'].mode()[0]
df['birthDate'].fillna(mode_date,inplace=True)


# In[27]:


df.isnull().sum()


# In[28]:


df = df[df['firstName'].notna()]


# In[29]:


df.isnull().sum()


# In[30]:


df.to_csv('cleaned_billionaires.csv', index=False)


# #  **2. Exploratory Data Analysis (EDA):**

# In[31]:


# Analyze Net Worth Distribution:

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['finalWorth'], kde=True)
plt.title('Distribution of Billionaire Net Worth')
plt.show()


# In[ ]:





# In[32]:


# Top 10 countries by number of billionaires By Country, Industry :


top_countries = df['country'].value_counts().nlargest(10).index
df_top_countries = df[df['country'].isin(top_countries)]

sns.boxplot(x='country', y='finalWorth', data=df_top_countries)
plt.xticks(rotation=45)
plt.title('Net Worth by Top 10 Countries')
plt.tight_layout()
plt.show()

# Top 10 industries by number of billionaires
top_industries = df['industries'].value_counts().nlargest(10).index
df_top_industries = df[df['industries'].isin(top_industries)]

sns.boxplot(x='industries', y='finalWorth', data=df_top_industries)
plt.xticks(rotation=45)
plt.title('Net Worth by Top 10 Industries')
plt.tight_layout()
plt.show()


# In[33]:


# Correlation with Country-Specific Metrics:
corr_cols = ['finalWorth', 'gdp_country', 'life_expectancy_country', 'tax_revenue_country_country']
corr = df[corr_cols].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[34]:


# Billionaire Distribution by Age, Gender :
sns.countplot(data=df, x='gender')
plt.title('Distribution by Gender')
plt.show()

sns.histplot(data=df, x='age', bins=20)
plt.title('Distribution by Age')
plt.show()


# In[40]:


# Most Common Industries and Self-Made Comparison:
top_industries = df['industries'].value_counts().head(10)
top_industries.plot(kind='bar', title='Top 10 Industries')
plt.show()

sns.countplot(data=df, x='industries', hue='selfMade')
plt.xticks(rotation=90)
plt.title('Self-Made Billionaires by Industry')
plt.show()


top_20 = df.sort_values(by='finalWorth', ascending=False).head(20)

plt.figure(figsize=(12, 8))
sns.barplot(data=top_20, x='finalWorth', y='personName', hue='selfMade')
plt.title('Top 20 Billionaires: Self-Made Status')
plt.xlabel('Net Worth (in Billions)')
plt.ylabel('Billionaire Name')
plt.legend(title='Self Made')
plt.tight_layout()
plt.show()




# In[36]:


# Country’s Economic Indicators vs Wealth:

sns.scatterplot(data=df, x='gdp_country', y='finalWorth')
plt.title('Billionaire Wealth vs Country GDP')
plt.xlabel('Country GDP (in USD)')
plt.ylabel('Billionaire Net Worth (in USD billions)')
plt.show()

sns.scatterplot(data=df, x='cpi_country', y='finalWorth')
plt.title('Billionaire Wealth vs Consumer Price Index (CPI)')
plt.xlabel('CPI Score')
plt.ylabel('Billionaire Net Worth (in USD billions)')
plt.show()


# In[37]:


cols = ['finalWorth', 'gdp_country', 'life_expectancy_country', 'tax_revenue_country_country', 'current_age']
corr = df[cols].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[38]:


#  Billionaire's wealth vs GDP

sns.scatterplot(data=df, x='gdp_country', y='finalWorth')
plt.title('Billionaire Wealth vs Country GDP')
plt.xlabel('Country GDP (in USD)')
plt.ylabel('Billionaire Net Worth (in USD billions)')
plt.show()


# In[ ]:




