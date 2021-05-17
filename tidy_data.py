#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
from pydataset import data


# ### 1.) Attendance Data
# 
# - Load the attendance.csv file and calculate an attendnace percentage for each student. One half day is worth 50% of a full day, and 10 tardies is equal to one absence.
# 
# - You should end up with something like this:

# name
# - Billy    0.5250
# - Jane     0.6875
# - John     0.9125
# - Sally    0.7625
# - Name: grade, dtype: float64

# ### Pivot better for visualization, Melt is better for aggregation!!

# In[14]:


attendance_df = pd.read_csv('untidy-data/attendance.csv')
# we want to calculate the attendance percentage count/total 1/2 day is 50%, 10T = 1A


# In[15]:


attendance_df.shape


# In[16]:


attendance_df.head()


# In[17]:


attendance_df.columns


# In[22]:


attendance_df = attendance_df.rename(columns = {'Unnamed: 0': 'name'})


# In[26]:


attendance_melt = attendance_df.melt(id_vars = 'name')


# In[27]:


attendance_melt.shape


# In[28]:


attendance_melt.head()


# In[38]:


conditions = [
    (attendance_melt['value'] == 'P'),
    (attendance_melt['value'] == 'T'),
    (attendance_melt['value'] == 'A'),
    (attendance_melt['value'] == 'H')
]

values = [1,.9,0,0.5]

#df.loc[df['att'] == 'P', 'percent'] = 1 another method


# In[39]:


attendance_melt['attendance_value'] = np.select(conditions,values)


# In[61]:


attendance_melt.head(5)


# In[40]:


attendance_percent = attendance_melt.groupby('name').attendance_value.mean()


# In[41]:


attendance_percent


# ### 2.) Coffee Levels
# - Read the coffee_levels.csv file.
# - Transform the data so that each carafe is in it's own column.
# - Is this the best shape for the data?

# In[44]:


coffee_levels_df = pd.read_csv('untidy-data/coffee_levels.csv')
coffee_levels_df.head(5)


# In[45]:


coffee_levels_df.shape


# In[ ]:





# In[53]:


coffee_levels_df_pivot = coffee_levels_df.pivot(index = 'hour', columns = 'coffee_carafe', values = 'coffee_amount')


# In[55]:


coffee_levels_df_pivot.shape


# In[57]:


coffee_levels_df_pivot


# In[60]:


coffee_levels_df.groupby('coffee_carafe').coffee_amount.mean()


# In[ ]:


# However if you are wanting to aggregate the above method is prefered
# I believe this is not the best shape to communicate the hourly coffee_amount consumed.
# Below is more ideal for visual.


# In[58]:


coffee_levels_df_pivot.T


# ### 3.) Cake Recipes
# - Read the cake_recipes.csv data. This data set contains cake tastiness scores for combinations of different recipes, oven rack positions, and oven temperatures.
# - Tidy the data as necessary.
# - Which recipe, on average, is the best? recipe b
# - Which oven temperature, on average, produces the best results? 275
# - Which combination of recipe, rack position, and temperature gives the best result? recipe b, bottom rack, 300 degrees

# In[95]:


cake_recipes_df = pd.read_csv('untidy-data/cake_recipes.csv')
cake_recipes_df.head(5)


# In[96]:


cake_recipes_df_melt = cake_recipes_df.melt(id_vars = 'recipe:position')
cake_recipes_df_melt


# In[100]:


# need to split the recipe and positon!!!!
cake_recipes_df_melt[['recipe', 'position']] = cake_recipes_df_melt['recipe:position'].str.split(':', expand = True)


# In[76]:


# dropped columns here....


# In[102]:


cake_recipes_df_melt.head()


# In[104]:


cake_recipes_df_melt.info()


# In[105]:


cake_recipes_df_melt = cake_recipes_df_melt.drop(columns = 'recipe:position')


# In[111]:


cake_recipes_df_melt.head()


# In[164]:


cake_recipes_df_melt.rename(columns={'variable': 'temperature', 'position': 'rack_position'}, inplace=True)


# In[ ]:


# table has been tidy up!!! renamed columns.


# In[165]:


cake_recipes_df_melt


# In[135]:


cake_recipes_df_melt.groupby('recipe').value.agg('mean')


# In[166]:


cake_recipes_pivot = cake_recipes_df_melt.pivot_table(index = ['recipe', 'rack_position'], columns = ['temperature'], values = 'value').reset_index()
cake_recipes_pivot


# In[136]:


# Which recipe, on average, is the best? recipe b
cake_recipes_df_melt.groupby('recipe').value.agg('mean')


# In[147]:


# Which oven temperature, on average, produces the best results? 275

cake_recipes_df_melt.groupby('temperature').value.agg('mean')


# In[ ]:


#Which combination of recipe, rack position, and temperature gives the best result? 
#recipe b, bottom rack, 300 degrees
#used a mask to solve for this issue. needed column associated with this row.
#Two methods to solve below:


# In[167]:


print(cake_recipes_df_melt[cake_recipes_df_melt.value == cake_recipes_df_melt.value.max()]) 


# In[168]:


cake_recipes_df_melt.loc[cake_recipes_df_melt.value == cake_recipes_df_melt.value.max()]

