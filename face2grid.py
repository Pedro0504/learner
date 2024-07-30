# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:36:22 2024

@author: pedro
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-01-2021.csv')
dt = df.loc[:,['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
#Create the figure
fig, ax = plt.subplots(figsize= (20,20))
#Add axes/subplots using subplot2grid
ax1 = plt.subplot2grid(shape= (3,3), loc= (0,0), rowspan = 3)
ax2 = plt.subplot2grid(shape= (3,3), loc= (0,1), rowspan = 3)
ax3 = plt.subplot2grid(shape= (3,3), loc= (0,2))
ax4 = plt.subplot2grid(shape= (3,3), loc= (1,2))
ax5 = plt.subplot2grid(shape= (3,3), loc= (2,2))

#Add ax1 to show data
ax1.scatter(dt['Country_Region'],dt['Confirmed'], marker='_', c='green' )
ax1.set_xlim(0,5)
ax1.set_ylim(20000,150000)
ax1.set_title('Confirmed')
ax1.grid()
#add data to ax2
ax2.scatter(dt['Country_Region'],dt['Deaths'], marker='_', c='red' )
ax2.set_xlim(0,50)
ax2.set_ylim(20000,50000)
ax2.set_title('Deaths')
ax2.grid()

plt.tight_layout()
plt.show()

df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['Month']= df_box['date'].dt.month
df_box['Day']= df_box['date'].dt.day
df_box['Year']= df_box['date'].dt.year

df_box = df_box.loc[:,['Year','Month','Page Views']].groupby(['Year','Month'])[['Page Views']].mean()
df_box.reset_index(inplace= True)
df_box['Month'] = pd.to_datetime(df_box['Month'], format='%m').dt.month_name()

print(df_box)
#Create the figure
fig, ax = plt.subplots(figsize= (10,10))
#Add axes/subplots using subplot2grid
ax1 = plt.subplot2grid(shape= (3,3), loc= (0,0), rowspan = 1)
ax2 = plt.subplot2grid(shape= (3,3), loc= (0,1), rowspan = 1)

#agregar valores
ax1.scatter(df_box['Year'], df_box['Page Views'], marker = '_')
ax1.set_xlim(0,5)
ax1.set_ylim(0,200000)
ax1.set_title('Year-wise Box Plot (Trend)')
ax1.grid()

ax2.scatter(df_box['Month'], df_box['Page Views'], marker = '_')
ax2.set_xlim(0,12)
ax2.set_ylim(0,200000)
ax2.set_title('Month-wise Box Plot (Seasonality)')
ax2.grid()

plt.tight_layout()
plt.show()




