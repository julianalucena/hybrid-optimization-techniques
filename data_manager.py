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
  f.write('111111\n') # adding feature types just for now
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


def process_data(processed_data, training_percentage):
  """
  Divide the dataset in training set and test set based on the percentage

  @type processed_data: dict
  @param processed_data: Tha data extracted from the dataset
  @type training_percentage: int
  @param training_percentage: The percentage used to divide the dataset

  @rtype: tuple
  @returns: The training set and the test set
  """

  print training_percentage, '%', 'training and', 100 - training_percentage, '%', 'test'

  len_test = 0

  test = dict()
  training = dict()

  for c, l in processed_data.items():
    training_quantity = (training_percentage*len(l)) / 100

    for i in range(training_quantity):

      if i == 0:
        training[c] = [l.pop(random.randint(0, len(l)-1))]
      else:
        training[c].append(l.pop(random.randint(0, len(l)-1)))

    test[c] = l

  return (training, test)

def get_infos(path):
  for i in range(5):
    dataset_path = path + "/sub_training_%i" % i
    training_path = path + "/training_%i" % i
    test_path = path + "/test_%i" % i

    print '\nfold %i' % i
    print 'database:'
    dataset = get_data(dataset_path)
    try:
      print 'Class 1:', len(dataset['1'])
    except KeyError:
      print 0
    try:
      print 'Class 2:', len(dataset['2'])
    except KeyError:
      print 0

    print '\ntraining:'
    training = get_data(training_path)
    try:
      print 'Class 1:', len(training['1'])
    except KeyError:
      print 0
    try:
      print 'Class 2:', len(training['2'])
    except KeyError:
      print 0

    print '\ntest:'
    test = get_data(test_path)
    try:
      print 'Class 1:', len(test['1'])
    except KeyError:
      print 0
    try:
      print 'Class 2:', len(test['2'])
    except KeyError:
      print 0

if __name__ == '__main__':
  #print get_data('datasets/sub_training_0')
  #data = {'1': [[92.0, 80.0, 10.0, 26.0, 20.0, 6.0, '1'],
  #  [91.0, 68.0, 27.0, 26.0, 14.0, 16.0, '1']],
  #  '2': [[91.0, 69.0, 25.0, 25.0, 66.0, 8.0, '2'],
  #    [92.0, 108.0, 53.0, 33.0, 94.0, 12.0, '2'],
  #    [89.0, 63.0, 24.0, 20.0, 38.0, 0.5, '2']]}
  #push_data(data, 'datasets/data')
  #folds_data = [get_data('datasets/liver/folds/oss/sub_training_%i' % i)
                  #for i in range(0, 5)]
  #for data in folds_data:
    #train, test = process_data(data, 80)
    #push_data(train, 'datasets/liver/folds/oss/training_%i' %
                      #folds_data.index(data))
    #push_data(test, 'datasets/liver/folds/oss/test_%i' %
                      #folds_data.index(data))
   get_infos('datasets/liver/selected/ib2')
