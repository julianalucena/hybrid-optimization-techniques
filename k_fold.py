#!/usr/bin/python
#-*- coding:utf-8 -*-

import random

"""
Do the separation into k-folds
"""

__author__ = 'Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def k_fold(path):
  folds = [open('sub_training_%i' % i, 'w') for i in range(0, 5) ]
  insts = open(path).readlines()

  while len(insts) != 0:
    for fold in folds:
      if len(insts) != 0:
        fold.write(insts.pop(random.randint(0, len(insts) - 1)))
      else:
        break

if __name__ == '__main__':
  k_fold('datasets/liver/bupa.data')
