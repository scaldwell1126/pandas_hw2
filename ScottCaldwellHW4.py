#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file  = "Resources/purchase_data.json"

# Read Purchasing File and store into Pandas data frame
df = pd.read_json(file)
df.head()


# ## Player Count

# * Display the total number of players
# 

# In[15]:


total_players = df["SN"].nunique()
player_count = pd.DataFrame({"Total Players" : [total_players]})
player_count


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[16]:


item = df['Item ID'].nunique()
avg_price = df['Price'].mean()
purchases = df['Item Name'].count()
total_rev = df['Price'].sum()
summary_df = pd.DataFrame({"Number of Unique Items" : [item],
                          "Average Price" : [avg_price],
                          "Number of Purchases" : [purchases],
                          "Total Revenue" : [total_rev]})
summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[53]:


#Gender Demo
#Male Percent 
male = df.loc[df['Gender'] == 'Male']
male_count = male['SN'].nunique()
total = df['Gender'].count()
male_perc = (male_count/total_players) * 100


#Female Percent 
female = df.loc[df['Gender'] == 'Female']
female_count = female['SN'].nunique()
female_perc = (female_count/total_players) * 100
female_perc

#Other Count and Percent 
df['Gender'].value_counts()
other = df.loc[df['Gender'] == 'Other / Non-Disclosed']
other_count = other['SN'].nunique()
other_perc = (other_count/total) * 100
other_perc

gender_df = pd.DataFrame({"Gender" : ["Male", "Female", "Other"],
                          "Total Count" : [male_count, female_count, other_count],
                         "Percentage of Players" : [male_perc, female_perc, other_perc] })
gender_df


# In[ ]:





# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[54]:


#Female Purchase Analysis 
female_purchase = female['Item Name'].count()
female_purchase
f_avg_price = female['Price'].mean()
f_total = female['Price'].sum()
price_per_f = (female_count/f_total)
price_per_f

#Male Purchase Analysis 
male_purchase = male['Item Name'].count()
male_purchase
m_avg_price = male['Price'].mean()
m_total = male['Price'].sum()
price_per_m = (m_total/male_count)
price_per_m

#Other Purchase Analysis 
other_purchase = other['Item Name'].count()
other_purchase
o_avg_price = other['Price'].mean()
o_total = other['Price'].sum()
price_per_o = (o_total/other_count)
price_per_o

purchase_df = pd.DataFrame({"Gender" : ["Female", "Male","Other"],
                           "Purchase Count" : [female_purchase, male_purchase, other_purchase],
                           "Average Purchase Price" : [f_avg_price, m_avg_price, o_avg_price],
                           "Total Purchase Value" : [f_total, m_total, o_total],
                           "Avg Total Price per Person" : [price_per_f, price_per_m, price_per_o]})
purchase_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[188]:


bins = [0, 9.90, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 9999]
labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

df['Age Ranges'] = pd.cut(df['Age'], bins=bins, labels=labels)
age_group = df.groupby(["Age Ranges"])
age_group
total_count_age = age_group["SN"].nunique()
total_count_age
percentage_by_age = (total_count_age/total_players) * 100
percentage_by_age
age_df = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})
age_df


# In[ ]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[191]:


purchase_count = age_group["Item ID"].count()
purchase_count
avg_price_age = age_group['Price'].mean()
avg_price_age
purchase_total = age_group["Price"].sum()
purchase_total
avg_purchase_age = avg_purchase_total/total_count_age

purchase_df = pd.DataFrame({"Purchase Count": purchase_count,
                                 "Average Purchase Price": avg_price_age,
                                 "Total Purchase Value": purchase_total,
                                 "Average Purchase Total per Person": avg_purchase_age})

purchase_df


# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[184]:


top_spenders = df.groupby("SN")

purchase_count = spender_stats["Item ID"].count()

avg_purchase_price_spender = spender_stats["Price"].mean()

purchase_total_spender = spender_stats["Price"].sum()

top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})

top_spenders_format = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

top_spenders_format


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[179]:


item = df[["Item ID", "Item Name", "Price"]]

item_group = item.groupby(["Item ID","Item Name"])

count_of_purchase = item_group['Price'].count()
item_value = item_group["Price"].sum()

item_price = item_value/count_of_purchase

item_df = pd.DataFrame({"Purchase Count": count_of_purchase, 
                                   "Item Price": item_price,
                                   "Total Purchase Value": item_value})
item_df_format = item_df.sort_values(["Total Purchase Value"] , ascending = False).head()
item_df_format


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[185]:


profit_df_format = item_df.sort_values(["Total Purchase Value"],
                                    ascending=False).head()
profit_df_forma


# In[186]:


profit_df_format


# In[ ]:




