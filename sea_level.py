# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:14:17 2024

@author: pedro
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import linregress

df_sea = pd.read_csv('epa-sea-level.csv')
x = df_sea['Year']
y = df_sea['CSIRO Adjusted Sea Level']


# Create scatter plot
plt.scatter(x = x, y = y)
#find the first line of best fit

reg = linregress(x,y)


x_p = pd.Series([i for i in range(1880, 2014)])
y_p = reg.slope*x_p + reg.intercept
plt.plot(x_p, y_p)
print(y_p)

#second

sec_df = df_sea[df_sea['Year']>=2000]
sec_x = sec_df['Year']
sec_y = sec_df['CSIRO Adjusted Sea Level']
sec_reg = linregress(sec_x, sec_y)
x_sp = pd.Series([i for i in range(2000, 2051)])
y_sp = sec_reg.slope*x_sp +sec_reg.intercept
plt.plot(x_sp, y_sp)
#ax name and title

plt.xlabel('Year')
plt.ylabel('Sea Level (Inches)')

plt.title('Rise of Sea Level')


