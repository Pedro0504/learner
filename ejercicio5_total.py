# -*- coding: utf-8 -*-
"""
Created on Sun May 19 08:37:01 2024

@author: pedro
"""

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

doc = pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-01-2021.csv')
dt_doc = pd.DataFrame(doc)

"""5_1. Mostrar la suma de los valores faltantes"""
def show_Nan(dt_doc):
    no_nan =  dt_doc.isnull().sum()
    return no_nan
#print(show_Nan(dt_doc))


"""5_2 crear una función que entrega los datos totales 
de casos confirmados, fallecidos, recuperados y activos
 por países """
print('--DATOS TOTALES POR PAÍSES--')
def datos_totales():
    sumaf = dt_doc.groupby(['Country_Region']).sum()
    data = ''
    r = input('Diga los datos que desea(Confirmados, Fallecidos,Recuperados y Activos):\n')
    if r == 'Confirmados':
        data = 'Confirmed'
    elif r == 'Fallecidos':
        data = 'Deaths'
    elif r == 'Recuperados':
        data = 'Recovered'
    elif r == 'Activos':
        data = 'Active'
    else:
        print('Los datos que pide no están disponibles.')
    return sumaf.loc[:,data]
#print(datos_totales())
"""5_3. Crear programa que obtenga la lista de provincias y el país
al que pertenecen pero solo de aquellas donde no haya casos
de pacientes recuperados"""
def proSt_sinRec():
    ps_F = dt_doc[dt_doc['Recovered']==0]
    ps_doc = ps_F.loc[:,['Province_State', 'Country_Region']]
    return ps_doc
#print(proSt_sinRec())

"""5_4. Defina una función que obtenga la información: país, 
confirmados, fallecidos y pacientes recuperados de los 10 países
con más pacientes confirmados."""
def maxim_Conf():
    e_nec = dt_doc.loc[:,['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    m_con = e_nec.sort_values(['Confirmed'], ascending = [False])
    return m_con.head(10)
#print(maxim_Conf())

"""5_5. Crear un programa que genere un gráfico de barras
en el que se muestre el total de casos confirmados, fallecidos
y recuperados, pero solo de aquellos países cuyo número 
de fallecidos sea inferior a 150."""
def graf_mfall():
    doc_sl = dt_doc.loc[:,['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    d_dta = doc_sl[doc_sl['Deaths']<150]
    d_dta = d_dta.head(3)
    dt = pd.melt(d_dta,id_vars =['Country_Region'], value_vars=['Confirmed', 'Deaths', 'Recovered'], var_name = 'variable', value_name='valor')
    return sns.FacetGrid(dt, row = 'variable', col='Country_Region',hue = 'Country_Region').map(sns.barplot, 'valor')

#print(graf_mfall())

"""5_6 crearás un dataframe de cada archivo csv. Tras ello,
 crearás un programa que  visualice la evolución de los casos
 confirmados, recuperados y fallecidos de COVID en el mundo.
 Teniendo en cuenta que: 
     El eje Y del gráfico deberá representar los valores 
     de los casos.
     El eje X del gráfico deberá representar los meses de los casos 
     (Enero, Febrero, Marzo)
     A través de las opciones pertinentes del gráfico elegido
     deberás diferenciar los tipos de casos
     El gráfico deberá incluir como título el siguiente texto
     "Evolución COVID primer trimestre 2021". """
"""Primero leer todos los csv , archivarlos en variables
seleccionando solo las colummnas que se necesitan"""
arch1 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-01-2021.csv',usecols= ['Country_Region','Confirmed', 'Deaths', 'Recovered']))
arch2 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-02-2021.csv',usecols= ['Country_Region','Confirmed', 'Deaths', 'Recovered']))
arch3 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-03-2021.csv',usecols= ['Country_Region','Confirmed', 'Deaths', 'Recovered']))
"""Luego crear dataframes para cada uno de los casos por meses."""
con = pd.DataFrame({'enero':[arch1['Confirmed'].sum()],'febrero': [arch2['Confirmed'].sum()], 'marzo': [arch3['Confirmed'].sum()]}, index= ['Confirmed'])
fal = pd.DataFrame({'enero':[arch1['Deaths'].sum()],'febrero': [arch2['Deaths'].sum()], 'marzo': [arch3['Deaths'].sum()]}, index = ['Deaths'])
rec = pd.DataFrame({'enero':[arch1['Recovered'].sum()],'febrero': [arch2['Recovered'].sum()], 'marzo': [arch3['Recovered'].sum()]}, index= ['Recovered'])
"""Se utiliza la función concat para unir los dataframes 
y se reutiliza el índice como nueva columna 'Casos"""
fin = pd.concat([con, fal, rec], axis =0)
fin = fin.rename_axis('Casos').reset_index()
"""Por  último la función melt modifica el dataframe en una forma
más cómoda de graficar, para utilizar la función catplot sobre
la nueva tabla"""
gra = fin.melt('Casos', var_name = 'Mes', value_name= 'Valor')
print(sns.catplot(data=gra, x = 'Mes', y = 'Valor',hue = 'Casos', kind = 'bar').set(title='Evolución COVID primer trimestre 2021'))


"""Ejercicio 5_7. Generar un dataframe de cada archivo csv. Tras 
ello. crearás un programa  que muestre la evolución de los casos 
confirmados y recuperados de COVID en las diferentes provincias
 de España, durante el primer trimestre de 2021"""
arch4 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-01-2021.csv',usecols= ['Country_Region','Province_State','Confirmed', 'Recovered']))
arch5 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-02-2021.csv',usecols= ['Country_Region','Province_State','Confirmed', 'Recovered']))
arch6 = pd.DataFrame(pd.read_csv('C:/Users/pedro/Desktop/DEPARTAMENTO/1MASTERD/SOLUCIÓN IV/TRABAJO_FINAL/csv_final/COVID_01-03-2021.csv',usecols= ['Country_Region','Province_State','Confirmed', 'Recovered']))
"""Se extraen las columnas que se necesitaran con máscaras basadas en las filas que tengan
como país a España, se utiliza la función drop() para eliminar las
columnas que no se necesitan, se concatenan y se limitan nuevamente 
a los datos que se presentan en el gráfico"""
cspE = arch4[arch4['Country_Region']=='Spain'].drop('Country_Region', axis=1)

cspF = arch5[arch5['Country_Region']=='Spain'].drop('Country_Region', axis=1).drop('Province_State', axis=1)

cspM = arch6[arch6['Country_Region']=='Spain'].drop('Country_Region', axis=1).drop('Province_State', axis=1)
"""Se  almacenan en datasets separados los casos confirmados
y los recuperados para presentarlos en tablas distintas,
se utiliza melt() para reorganizar la información y luego
catplot para presentar cada información"""
con_t = pd.concat([cspE[['Province_State','Confirmed']], cspF['Confirmed'], cspM['Confirmed']], axis=1)
con_t.columns =['Province', 'Enero','Febrero', 'Marzo']
gdc = con_t.melt('Province', var_name= 'Mes', value_name = 'Confirmados')
print('--CONFIRMADOS--')
print(sns.catplot(data=gdc, x= 'Mes', y = 'Confirmados', hue = 'Province', kind = 'bar').set(title=('Casos Confirmados Primer Trimestre 2021')))

rec_t = pd.concat([cspE[['Province_State','Recovered']], cspF['Recovered'], cspM['Recovered']], axis=1)
rec_t.columns =['Province', 'Enero','Febrero', 'Marzo']
gdr = con_t.melt('Province', var_name= 'Mes', value_name = 'Recuperados')
print('--RECUPERADOS--')
print(sns.catplot(data=gdr, x= 'Mes', y = 'Recuperados', hue = 'Province', kind = 'bar').set(title=('Casos Recuperados Primer Trimestre 2021')))

