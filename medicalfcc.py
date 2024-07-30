# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:45:16 2024

@author: pedro
"""

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

doc = pd.read_csv('./medical_examination.csv')
dt_doc = pd.DataFrame(doc)
weight = dt_doc['weight']
height = dt_doc['height']
over = [weight/((height/100)**2)]
over = over[0]>25
over = over.replace({True:1,False:0})
doc['overweight']=over
#3
normcol = doc['cholesterol']>1
normcol = normcol.replace({True:1,False:0})
normglu = doc['gluc']>1
normglu = normglu.replace({True:1,False:0})
doc['cholesterol']= normcol
doc['gluc']= normglu

#4
def cat_plot(df):
    
    df_ct= doc[['cardio','cholesterol','gluc','smoke','alco', 'active', 'overweight']]
    df_cat = df_ct.melt('cardio', var_name = 'variable', value_name ='total')
    fig = sns.catplot(df_cat, x = 'variable', kind= 'count', col='cardio', hue = 'total')
    fig.set_axis_labels('variable', 'total')
    return df_cat
#print(cat_plot(doc))
df = doc

def heat_mapu(doc):
    df_heat = df[df['ap_lo']<=df['ap_hi']]
    df_heat = df[df['height']>=df['height'].quantile(0.025)]
    df_heat = df[df['height']<=df['height'].quantile(0.975)]
    df_heat = df[df['weight']>=df['weight'].quantile(0.025)]
    df_heat = df[df['weight']<=df['weight'].quantile(0.975)]
    corr = df_heat.corr()
    
    mask = np.triu(corr)
    
    fig, ax= plt.subplots(figsize=(10,10))
    
    return sns.heatmap(corr, linewidths=1,annot = True,fmt = '.1f' , square=True, mask = mask, cbar_kws = {'shrink':0.5})
print(heat_mapu(df))

def heat_map(doc):
    df_heat = df[
        (df['ap_lo']<=df['ap_hi']) &
        (df['height']>= df['height'].quantile(0.025))&
        (df['height']<= df['height'].quantile(0.975))&
        (df['weight']>= df['weight'].quantile(0.025))&
        (df['weight']<= df['weight'].quantile(0.975))
    ]
    corr = df_heat.corr()
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize = (10,10))
    fig = sns.heatmap(corr, mask= mask, annot=True, fmt = '.1f')
    return fig
print(heat_map(df))
     




