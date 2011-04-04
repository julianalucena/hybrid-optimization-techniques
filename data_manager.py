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

def push_data(data, path):
  f = open(path, 'w')
  data_compressed = list()

  for klass in data.keys():
    data_compressed.extend([inst for inst in data[klass]])

  for a in range(0, len(data_compressed)):
    i = random.randint(0, len(data_compressed) - 1)
    inst = data_compressed.pop(i)
    for attr in inst:
      f.write(str(attr))
      if attr == inst[-1]:
        f.write('\n')
      else:
        f.write(',')

if __name__ == '__main__':
  print get_data('datasets/sub_training_0')
  data = {'1': [[92.0, 80.0, 10.0, 26.0, 20.0, 6.0, '1'],
    [91.0, 68.0, 27.0, 26.0, 14.0, 16.0, '1']],
    '2': [[91.0, 69.0, 25.0, 25.0, 66.0, 8.0, '2'],
      [92.0, 108.0, 53.0, 33.0, 94.0, 12.0, '2'],
      [89.0, 63.0, 24.0, 20.0, 38.0, 0.5, '2']]}
  push_data(data, 'datasets/data')
