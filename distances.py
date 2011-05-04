#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import sqrt, fabs

"""
All distances used in the experiment
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def euclidian_distance(a, b, solution):
	"""
	Calculates Euclidian Distance of two vectors with numerical attributes
	
	@type a: list
	@param a: The vector
	@type b: list
	@param b: The other vector	
	
	@rtype: float
	@returns: The Euclidian Distance between a and b
	"""
	
	s = 0.0
	
	# Tirando label
	for i, ai in enumerate(a[:-1]):
                if solution[1][i]:
			wx = solution[0][i]
			s = s + (fabs(ai*wx - b[i]*wx)**2)
	
	return sqrt(s)
	
def manhattan_distance(a, b, solution):
	"""
	Calculates Manhattan Distance of two vectors with numerical attributes
	
	@type a: list
	@param a: The vector
	@type b: list
	@param b: The other vector	
	
	@rtype: float
	@returns: The Manhattan Distance between a and b
	"""
	
	s = 0.0

	# Tirando label
	for ai in a[:-1]:
		i = a.index(ai)
		if solution[1][i]:
			wx = solution[0][i]
			s = s + fabs(ai*wx - b[i]*wx)
	
	return s
	
def adaptative_distance(a, b, distance_metric, training_set, solution):	
	"""
	Calculates Adaptative Distance of two vectors with numerical attributes
	
	@type a: list
	@param a: The vector
	@type b: list
	@param b: The other vector
	@type distance_metric: function
	@param distance_metric: The function used to calculate the distances
	
	@rtype: float
	@returns: The Adaptative Distance between a and b
	"""
	
	return distance_metric(a, b, solution) / __min_sphere_radius(b, training_set, distance_metric, solution)
	
def __min_sphere_radius(a, training_set, distance_metric, solution):
	"""
	Calculates the minimun distance between 
	
	@type a: list
	@param a: The vector to center the sphere
	@type dataset: dict
	@param dataset: The dataset with all instances
	@type distance_metric: function
	@param distance_metric: The function used to calculate the distances
	
	@rtype: float
	@returns: The minimun radius sphere centered in a that ...
	"""
	
	e = 0.01 #e > 0 is an arbitrarily small number
	
	distances = list()
	
	for c, l in training_set.items():
		if c != a[-1]:
			for li in l:
				distances.append(distance_metric(a, li, solution))

	distances.sort()
	
        if len(distances) != 0:
          return distances[0] - e
        else:
          return e
