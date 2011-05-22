#!/usr/bin/python
#-*- coding:utf-8 -*-

import random
import operator

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

def stratified_k_fold(path, k):
  insts = get_data(path)
  folds = [dict.fromkeys(insts.keys()) for i in range(0, k)]
  # Initializing because fromkeys() uses the reference
  for fold in folds:
    for klass in fold.keys():
      fold[klass] = []

  qtt_per_klass = map(len, [insts[klass] for klass in insts.keys()])
  qtt_per_fold = map(operator.idiv, qtt_per_klass, [k] * len(qtt_per_klass))
  qtt_leftover = map(operator.mod, qtt_per_klass, [k] * len(qtt_per_klass))

  # Distributing instances to folds
  klass_qtt_per_fold = dict(zip(insts.keys(), qtt_per_fold))
  for fold in folds:
    for (k, q) in klass_qtt_per_fold.items():
      for i in range(0, q):
        fold[k].append(insts[k].pop(random.randint(0, len(insts[k]) - 1)))

  # Distributing leftover instances to folds (inexact division)
  klass_qtt_leftover = dict(zip(insts.keys(), qtt_leftover))
  for (k, q) in klass_qtt_leftover.items():
    for i in range(0, q):
      f = sorted(folds, key=lambda fold: len(fold[k]))[0]
      f[k].append(insts[k].pop(random.randint(0, len(insts[k]) - 1)))

  # Printing just to be sure that all instances were used
  print insts
  for fold in folds:
    push_data(fold, 'test/sub_training_%i' % folds.index(fold))

if __name__ == '__main__':
  #k_fold('datasets/liver/bupa.data', 5)
  stratified_k_fold('datasets/ionosphere/ionosphere.data', 5)
