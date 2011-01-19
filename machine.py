# -*- coding: utf-8 -*-

#!/usr/bin/python
#-*- coding:utf-8 -*-

import operator
#import resource
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
	#print 'hits', hits
	#print 'len(test_set)', test_len
	#print hits
	return hits/test_len
	
if __name__ == "__main__":
	print 'Processing Balance Scale Database, considering numeric attributes'
	print 'Using k-NN'
	#print 'Using k-NN Weight'
	print ''
	#hit_rates = training_machine('datasets/iris.data', get_iris_data, euclidian_distance, 75)
	#hit_rates = training_machine('datasets/yeast.data', get_yeast_data, euclidian_distance, 95)
	
	hit_rates = training_machine('datasets/balance-scale.data', get_scale_data, euclidian_distance, 95)
	#hit_rates = training_machine('datasets/car.data', get_car_data, vdm, 95)
	
	#hit_rates = training_machine('datasets/tae.data', get_tae_data, hvdm, 95)
	#hit_rates = training_machine('datasets/abalone.data', get_abalone_data, hvdm, 99)

	plt.plot([1,2,3,5,7,9,11,13,15], hit_rates)
	plt.ylabel('Hit Rate')
	plt.xlabel('K Value')
	plt.axis([0, 16, 0, 95])
	plt.show()
