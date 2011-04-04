#!/usr/bin/python
#-*- coding:utf-8 -*-

import random

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

def stratified_k_fold(path, k):
  folds = [open('sub_training_%i' % i, 'w') for i in range(0, k) ]
  insts = open(path).readlines()
  qtd_insts = len(insts)/len(folds)
  leftover = len(insts) - k*qtd_insts

  for fold in folds:
    for i in range(0, qtd_insts):
      fold.write(insts.pop(random.randint(0, len(insts) - 1)))

  for i in range(0, leftover):
    folds[random.randint(0, len(insts) -1)].write(insts.pop(i))

if __name__ == '__main__':
  k_fold('datasets/liver/bupa.data', 5)
  stratified_k_fold('datasets/liver/bupa.data', 5)
