#!/usr/bin/python
#-*- coding:utf-8 -*-

import random

"""
The manager responsible for processing the datasets
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def get_data(path):
  instances = dict()

  with open(path) as f:
    f.readline() # removing first line just for now
    for line in f:
      inst = line.split(',')
      klass = inst[-1].rstrip('\n')
      inst = map(float, inst[:-1])
      inst.append(klass)
      if instances.has_key(klass):
        instances[klass].append(inst)
      else:
        instances[klass] = [inst]

  return instances

if __name__ == '__main__':
  print get_data('datasets/sub_training_0')
