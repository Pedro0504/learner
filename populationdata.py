# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:09:21 2024

@author: pedro
"""

import numpy as np
import pandas as pd


listas = [i for i in range(9)]
"""
def calculations(l):
    if len(l)<9:
        raise ValueError ('List must contain nine numbers')
    else:
        lf = np.array(l)
        l = lf.reshape(3,3)
        print(l)
        mean = [l.mean(axis=0).tolist(),l.mean(axis=1).tolist(),lf.mean().tolist()]
        variance = [l.var(axis =0).tolist(),l.var(axis=1).tolist(), lf.var().tolist()]
        stan = [l.std(axis =0).tolist(), l.std(axis=1).tolist(), lf.std().tolist()]
        maxi = [l.max(axis = 0).tolist(), l.max(axis=1).tolist(), lf.max().tolist()]
        mini = [l.min(axis = 0), l.min(axis=1), lf.min().tolist()]
        suma = [l.sum(axis = 0).tolist(), l.sum(axis=1).tolist(), lf.sum().tolist()]
    calculations ={'mean': mean,'variance': variance, 'standard deviation': stan, 'max':maxi, 'min':mini, 'sum': suma}
    return calculations
print(calculations(listas))
"""
#ejercicio 2 adult data
df = pd.read_csv('./adult.data.csv')
dfr = df['race'].value_counts()
#average men age
avam = df[['age','sex']]
avam = avam[avam['sex']=='Male']
ave = avam['age'].mean()

#3 percenteage of people with bachelor
deg =  df['education'].count()
bac = df[['education']]
bac = bac[bac['education']=='Bachelors']
bac = bac['education'].count()
percenteage_bachelors = round((bac/deg)*100,1)

#percenteage of bac, mast, doc
high = df[['education']]
ms = high[high['education']=='Masters']
mas = ms['education'].count()
dc = high[high['education']=='Doctorate']
doc = dc['education'].count()
comp = bac+mas+doc
higher = round((comp/deg)*100,1)
lower = round(((deg-comp)/deg)*100,1)

#percentage highest earning
ear = df[['education', 'salary']]
earn = ear[ear['salary']=='>50K']
total = earn['education'].count()
#bien
earm = earn[earn['education']=='Masters']
eam = earm['education'].count()
#ok
eard = earn[earn['education']=='Doctorate']
ead = eard['education'].count()
earb = earn[earn['education']=='Bachelors']
eab = earb['education'].count()
#ok
total_deg = eam+eab+ead
per_hig = round((total_deg/total)*100,1)
per_low = round(((total-total_deg)/total)*100, 1)
#5. minimun number of hours worked per week
hperw = df[['hours-per-week', 'salary']]
minh = df['hours-per-week'].min()
#percentage of minimun hour workers earning >50K
totm = hperw[hperw['hours-per-week']==minh]
tot = totm['hours-per-week'].count()
rtm = totm[totm['salary']=='>50K']['salary'].count()
perc = round((rtm/tot)*100,1)

#6. highest percentage country
cons = df[['native-country', 'salary']]
conh = cons[cons['salary']=='>50K']
cont = conh.groupby('native-country').value_counts().sort_values(ascending = False).reset_index()
mcont = cont['count'].max()
hicont = cont[cont['count']==mcont]
hcont = [i for i in hicont['native-country']]
country = hcont[0]



#last one

ocu = df[['salary', 'occupation', 'native-country']]
ind = ocu[ocu['native-country']=='India']
indo = ind[ind['salary']=='>50K']
india = indo.groupby('occupation').value_counts().sort_values(ascending = False).reset_index()
prof = india['count'].max()
lt = prof[prof['count']==prof]
var = [i for i in lt['occupation']]
 
print(india)



