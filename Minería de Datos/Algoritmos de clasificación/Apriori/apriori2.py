# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:21:19 2021

@author: Snv24
"""

from apriori_python import apriori
import pandas as pd

store_data = pd.read_csv('C:\\Users\\Snv24\\Desktop\\Apriori\\Dataset_preprocesado_sc.csv', header=None)
records = []
for i in range(0, 5):
    records.append([str(store_data.values[i,j]) for j in range(0, 19)])
    
for i in records:
    print(i)
    print()


freqItemSet, rules = apriori(records, minSup=0.05, minConf=0.05)

for i in rules:
    cad = str(i)
    if 'nan' not in cad:
        print(i)