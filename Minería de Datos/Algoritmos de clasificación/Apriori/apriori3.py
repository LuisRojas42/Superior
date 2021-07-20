# -*- coding: utf-8 -*-
"""
Created on Sun May 16 01:05:23 2021

@author: Snv24
"""

from efficient_apriori import apriori

def data_generator(filename):
  """
  Data generator, needs to return a generator to be called several times.
  Use this approach if data is too large to fit in memory. If not use a list.
  """
  def data_gen():
    with open(filename) as file:
      try:
        for line in file:
          yield tuple(k.strip() for k in line.split(','))      
      except:
          print()

  return data_gen

transactions = data_generator('C:\\Users\\Snv24\\Desktop\\Apriori\\Dataset_preprocesado_sc.csv')
itemsets, rules = apriori(transactions, min_support=0.7, min_confidence=0.7)

for i in rules:
    print(i)
    