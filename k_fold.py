#!/usr/bin/python
#-*- coding:utf-8 -*-

import random

from data_manager import *

"""
Do the separation into k-folds
"""

__author__ = 'Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def k_fold(path, k):
  folds = [open('sub_training_%i' % i, 'w') for i in range(0, k) ]
  insts = open(path).readlines()

  while len(insts) != 0:
    for fold in folds:
      if len(insts) != 0:
        fold.write(insts.pop(random.randint(0, len(insts) - 1)))
      else:
        break

# (Unfortunately) very specific to Liver dataset
def stratified_k_fold(path, k):
  folds = [{'1': [], '2': []}, {'1': [], '2': []}, {'1': [], '2': []},
      {'1': [], '2': []}, {'1': [], '2': []}]
  #folds = [open('sub_training_%i' % i, 'w') for i in range(0, k) ]
  #insts = open(path).readlines()
  insts = get_data(path)
  one = 142 # 42% 29 instances
  two = 199 # 58% 39 instances
  #map(len, [insts[klass]for klass in insts.keys()])
  qtd_insts = 341/len(folds)
  one_qtd = 28
  two_qtd = 39

  for fold in folds:
    for i in range(0, one_qtd):
      fold['1'].append(insts['1'].pop(random.randint(0, len(insts['1']) - 1)))
      #fold.write(insts.pop(random.randint(0, len(insts) - 1)))
    for i in range(0, two_qtd):
      fold['2'].append(insts['2'].pop(random.randint(0, len(insts['2']) - 1)))

  leftover_one = len(insts['1'])
  leftover_two = len(insts['2'])
  for i in range(0, leftover_one):
    print map(lambda fold: (len(fold['1']) + len(fold['2'])), folds)
    f = sorted(folds, key=lambda fold: (len(fold['1']) + len(fold['2'])))[0]
    print len(fold['1']) + len(fold['2'])
    f['1'].append(insts['1'].pop(random.randint(0, len(insts['1']) - 1)))

  for i in range(0, leftover_two):
    f = sorted(folds, key=lambda fold: (len(fold['1']) + len(fold['2'])))[0]
    f['2'].append(insts['2'].pop(random.randint(0, len(insts['2']) - 1)))

  print insts
  for fold in folds:
    print (len(fold['1']) + len(fold['2']))
    push_data(fold, 'sub_training_%i' % folds.index(fold))

if __name__ == '__main__':
  #k_fold('datasets/liver/bupa.data', 5)
  stratified_k_fold('datasets/liver/bupa.data', 5)
