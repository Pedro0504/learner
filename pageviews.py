# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:48:11 2024

@author: pedro
"""

#Visual Free code camp
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
#1.read csv and set date as index

df = pd.read_csv('./fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'].str.strip(),format = 'mixed')

df = df.set_index('date')
#2. clean data
df = df[df['value']>df['value'].quantile(0.025)]
df = df[df['value']<df['value'].quantile(0.975)]
df = df.rename(columns={'value':'Page Views'})
#3. Create a line plot with a sugested title 
line = sns.lineplot(data = df, x = 'date', y = 'Page Views').set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

#4.Create a barplot group by months
df_bar = df.copy()

df_bar.reset_index(inplace=True)
df_bar['Month']= df_bar['date'].dt.month
df_bar['Day']= df_bar['date'].dt.day
df_bar['Year']= df_bar['date'].dt.year

df_bar = df_bar.loc[:,['Year','Month','Page Views']].groupby(['Year','Month'])[['Page Views']].mean()
df_bar.reset_index(inplace= True)
df_bar['Month'] = pd.to_datetime(df_bar['Month'], format='%m').dt.month_name()
df_bar = df_bar.rename(columns ={'Page Views':'Average Page Views'})

barp = sns.barplot(data = df_bar,x = 'Year',y = 'Average Page Views', hue = 'Month')

#5. Prepare two box plot


df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

fig, (ax1, ax2)= plt.subplots(1,2, figsize= (20,5))
sns.boxplot(ax = ax1, x = 'year', y = 'Page Views', data = df_box)
ax1.set_xlabel('Year')
ax1.set_ylabel('Page Views')
ax1.set_title('Year-wise Box Plot (Trend)')

sns.boxplot(ax = ax2, x = 'month', y = 'Page Views', data = df_box)
ax2.set_xlabel('Month')
ax2.set_ylabel('Year')
ax2.set_title('Month-wise Box Plot (Seasonality)')

plt.show()



