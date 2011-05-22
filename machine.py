#!/usr/bin/python
#-*- coding:utf-8 -*-

import operator
from datetime import datetime

from data_manager import *
from classification_algorithms import *

"""
The machine responsible for classifier the examples
"""
__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'


def training_machine(training_set, test_set, knn_function, solution, adaptative=False):
    """
    Do the machine training

    @type data_path: str
    @param data_path: The data path to be processed
    @type process_data_method: methodname
    @param process_data_method: The method to be used to process the data
    @type calc_distance_method: methodname
    @param calc_distance_method: The function to be used to calculate the distance
    @type training_percentage: int
    @param training_percentage: The percentage to used to divide the dataset


    @rtype: list
    @returns: All hit rates
    """
    test_len = 0.0
    hits = 0.0
    for c, l in test_set.items():
        test_len = test_len + len(l)
        for i in l:
            i_class = knn_function(solution, training_set, i, adaptative=True)

            if i_class == c:
                hits = hits + 1
    return hits/test_len

if __name__ == "__main__":
    print 'Processing Balance Scale Database, considering numeric attributes'
    print 'Using k-NN'
    print ''
    hit_rates = training_machine('datasets/balance-scale.data', get_scale_data, euclidian_distance, 95)
    plt.plot([1,2,3,5,7,9,11,13,15], hit_rates)
    plt.ylabel('Hit Rate')
    plt.xlabel('K Value')
    plt.axis([0, 16, 0, 95])
    plt.show()
