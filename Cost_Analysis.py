
# coding: utf-8

# In[ ]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


def load_data(file_name):
    DATA_PATH = os.path.join(os.getcwd(),"data")
    data = pd.read_excel(os.path.join(DATA_PATH, file_name))
    
    new_index = data.reset_index() #add index row
    new_header = new_index.iloc[1] #identify a new header
    new_data = new_index[2:] #chop off top two rows
    new_data_index = new_data.reset_index(drop=True) #reset again
    new_data_clean = new_data_index.fillna('') #drop nan
    new_data_clean.columns = new_header

    return new_data_clean


# In[2]:


carpenters = ['Carpenter Foreman', 'Carpenter', 'Dockbuilder', 'Timberman']
laborers   = ['']
operators  = ['']
indirects  = ['']


def burn_rate(data, labor_type, date_1, date_2):
    descrip_1 = data['Description'].iloc[:,0] #reconfigure description 1
    descrip_2 = data['Description'].iloc[:,1] #reconfigure description 2
    df_d      = data[(data['Stamp'] > date_1)                    & (data['Stamp'] <= date_2)] #set the date range
    df_d1c    = df_d.groupby(descrip_2)['Amount'].sum() #groupby & sum by value
    
    return df_d1c.reindex(labor_type) #return groupset
    return df_d1c.reindex(labor_type).sum() #returns sum of groupset


# In[ ]:


# def load_data(file_name):
#     DATA_PATH = os.path.join(os.getcwd(),"data")
#     data = pd.read_excel(os.path.join(DATA_PATH, file_name))
    
#     return data


# In[26]:


# clean data by chopping off rows
# def clean_data(input):
#     new_index = input.reset_index() #add index row
#     new_header = new_index.iloc[1] #identify a new header
#     new_data = new_index[2:] #chop off top two rows
#     new_data_index = new_data.reset_index(drop=True) #reset again
#     new_data_clean = new_data_index.fillna('') #drop nan
#     new_data_clean.columns = new_header

#     return new_data_clean


# In[27]:


#monthy cost chart
def chart(input):
    new_frame = input[['Stamp','Amount']].copy() #timestamp + amount
    new_index = new_frame.set_index(pd.DatetimeIndex(new_frame['Stamp'])) #reset index
    month = new_index.resample('M').sum() #sum by month
    month_index = month.reset_index() #reset again
    date = month_index['Stamp']
    amount = month_index['Amount']
    plt.xticks(rotation=45)
    plt.bar(date, amount, 20)
    plt.show()
    
    return month_index


# In[ ]:


# #sum by cost code and extra
# df.groupby(['Cost Code', 'Extra']).sum().head()


# In[13]:


# chart(df)


# In[14]:


# def cost_period(input):
#     new_frame = input[['Stamp','Amount', 'Cost Code', 'Extra', 'Description']].copy() #timestamp + amount
#     new_index = new_frame.set_index(pd.DatetimeIndex(new_frame['Stamp'])) #reset index
#     month = new_index.loc['2018-09-24 01:00:00':'2019-1-31 04:00:00']

    
#     return new_index.head()


# In[15]:


# cost_period(df)


# In[16]:


# new_frame = df[['Stamp','Amount', 'Cost Code', 'Extra', 'Description']].copy() #timestamp + amount
# new_index = new_frame.set_index(pd.DatetimeIndex(new_frame['Stamp'])) #reset index


# In[17]:


# new_index.head()


# In[18]:


# total_cost = df['Amount'].sum()


# In[19]:


# #contract_amount = 1445727
# contract_amount = 7850000
# margin = contract_amount - total_cost
# percentage = margin/contract_amount
# print(total_cost)
# print(margin)
# print(percentage.round(3))


# In[20]:


# january = new_index.loc['2018-12-24 01:00:00':'2019-01-27 04:00:00']
# january.head()


# In[21]:


# january['Amount'].sum()


# In[22]:


# jan_codes = january.groupby(['Cost Code', 'Extra']).sum()
# jan_codes


# In[23]:


# jan_codes = jan_codes.sort_values(by='Amount', ascending=False)
# jan_codes['cum_sum'] = jan_codes.Amount.cumsum()
# jan_codes['cum_perc'] = 100*jan_codes.cum_sum/jan_codes.Amount.sum()
# jan_codes

