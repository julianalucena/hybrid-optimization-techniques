#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distances import *

"""
Contains all classifiers
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def knn(distance_metric, solution, training_examples, e, adaptative=False):
    """
    k-NN algorithm

    @type calc_distance_method: methodname
    @param calc_distance_method: The function to be used to calculate the distance
    @type k: int
    @param k: The quantity of neighbors
    @type training_examples: dict
    @param training_examples: The training set
    @type e: list
    @param e: The element to be classified


    @rtype: str
    @returns: The predicted class for the element
    """

    k = solution[2]
    # Calculating the distances
    distances = list()
    for c, l in training_examples.items():
        for i in l:
            if adaptative:
                d = adaptative_distance(e, i, distance_metric, training_examples, solution) # the order of 'e' and 'i' matters
            else:
                d = distance_metric(i, e, solution)

            distances.append((d, c))
    distances = sorted(distances)

    # Getting k near classes
    near_classes = dict()
    for ki in range(k):

      try:
        (d, i_class) = distances[ki]
        if near_classes.has_key(i_class):
            if near_classes[i_class][0] > d:
                near_classes[i_class] = (d, near_classes[i_class][1] + 1)
            else:
                near_classes[i_class] = (near_classes[i_class][0], near_classes[i_class][1] + 1)
        else:
            near_classes[i_class] = (d, 1)
          # Few instances for k number
      except IndexError:
        pass
    near_classes_ordered = list()
    for c, t in near_classes.items():
        near_classes_ordered.append((t[1], t[0], c))

    near_classes_ordered.sort()
    near_classes_ordered.reverse()
    return near_classes_ordered[0][2]

def knn_euclidian(solution, training_examples, e, adaptative=False):
    return knn(euclidian_distance, solution, training_examples, e, adaptative)

def knn_manhattan(k, training_examples, e, adaptative=False):
    return knn(manhattan_distance, k, training_examples, e, adaptative)

def knn_adaptative(k, training_examples, e, adaptative=False):
    return knn(adaptative_distance, k, training_examples, e, adaptative)
