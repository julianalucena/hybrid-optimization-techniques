#!/usr/bin/python
#-*- coding:utf-8 -*-

import random
from classification_algorithms import *
from data_manager import *
from machine import training_machine

from collections import deque
from math import ceil, sqrt, exp

"""
The hybrid algorithms
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'


def simulated_annealing(training_set, test_set, knn_function, initial_solution, f, i = 100, m = 10, n = 2, initial_temperature = 1, reduction_factor = 0.9, adaptative=False):
	"""
	Simulated annealing algorithm.

	@type training_set: dict
	@param training_set: the training dataset
	@type test_set: dict
	@param test_set: the test dataset
	@type knn_function: function
	@param knn_function: the function used to classify the examples
	@type initial_solution: tuple ([Weights], [Features], k)
	@param initial_solution: the initial solution ([1, ..., 1], [1, ..., 1], 1)
	@type i: int
	@param i: the number of iterations (default = 100)
	@type m: int
	@param m: number of random weights to be assigned to features (default = 10)
	@type n: int
	@param n: number of features to be assigned by weights (default = 2)
	@type initial_temperature: float
	@param initial_temperature: the initial temperature (default = 1)
	@type reduction_factor: float
	@param reduction_factor: the reduction factor used to decrease the temperature (default = 0.9)
	@type adaptative: bool
	@param adaptative: indicates when to use adaptative distance

	@rtype: tuple
	@returns: the best solution found by the algorithm
	"""
	
	best_solution = initial_solution
	temperature = initial_temperature
	
	# De 0 ate o numero de iteracoes
	f.write('SA, adaptative: %s \n' % adaptative)
	for it in range(i):
			print it
			f.write('iteracao %s \n' % it)
			# Gera uma nova solucao (new_solution) da melhor solucao atual (best_solution)
			p = int(ceil(sqrt(len(best_solution[0]))))
			solutions = __gen_neighbors_solutions(best_solution, m, n, p)
			(hit_rate, new_solution) = __best_solution(training_set, test_set, knn_function, solutions, adaptative)
			# Se o custo da nova solucao e menor que o custo da melhor solucao atual
			new_solution_cost = __cost(training_set, test_set, knn_function, new_solution)
			best_solution_cost = __cost(training_set, test_set, knn_function, best_solution)
			if new_solution_cost >= best_solution_cost:
					# A melhor solucao eh a nova solucao
					best_solution = new_solution
					f.write('%s \n' % str(best_solution))
					f.write('hit_rate: %s \n' % hit_rate)
			# Caso contrario, a nova solucao ainda tem chance de ser aceita
			else:
					# Calcula DeltaC, a variacao dos custos
					delta_c = abs(new_solution_cost - best_solution_cost)
					# Calcula o Metropolis Criteria (e^(-DeltaC/t))
					metropolis_criteria = exp(-delta_c / temperature)
					# Se esse criterio for maior que um numero aleatorio
					if metropolis_criteria >= random.random():
							# Aceita a nova solucao como a melhor solucao
							best_solution = new_solution
							f.write('if metropolis')
							f.write('%s \n' % str(best_solution))
							f.write('hit_rate: %s \n' % hit_rate)
			
			# A temperatura � atualizada em cada iteracao multipla de 10
			if (it % 10 == 0):
					# Diminui a temperatura pelo fator de reducao
					temperature = temperature * reduction_factor
	
	return best_solution


def __cost(training_set, test_set, knn_function, solution, adaptative=False):
	"""
	Calculates the cost of a given solution.
	In this case, calculates the accuracy rate of a k-NN.

	@type training_set: dict
	@param training_set: the training dataset
	@type test_set: dict
	@param test_set: the test dataset
	@type knn_function: function
	@param knn_function: the function used to classify the examples
	@type solution: tuple
	@param solution: the solution
	@type adaptative: bool
	@param adaptative: indicates when to use adaptative distance

	@rtype: float
	@returns: the cost of the given solution
	"""
	
	# Dado a solucao (configuracao de pesos/caracteristicas), transforma os , calcula o k-NN e retorna a taxa de acerto
	return training_machine(training_set, test_set, knn_function, solution, adaptative)

def tabu_search(training_set, test_set, knn_function, solution, i, f, adaptative=False):
	"""
	Tabu Search algorithm.

	@type training_set: dict
	@param training_set: the training dataset
	@type test_set: dict
	@param test_set: the test dataset
	@type knn_function: function
	@param knn_function: the function used to classify the examples
	@type initial_solution: tuple ([Weights], [Features], k)
	@param initial_solution: the initial solution ([1, ..., 1], [1, ..., 1], 1)
	@type i: int
	@param i: the number of iterations
	@type adaptative: bool
	@param adaptative: indicates when to use adaptative distance

	@rtype: tuple
	@returns: the best solution found by the algorithm
	"""
	
	s_ = solution
	tabu = deque()
	tabu.append(solution)

	m = 10
	n = 2
	p = int(ceil(sqrt(len(solution[0]))))
	t = p
	for it in range(i):
			  f.write('iteracao %s \n' % it)
			  print it
			  solutions = __gen_neighbors_solutions(s_, m, n, p)
			  (hit_rate, s_) = __best_solution(training_set, test_set, knn_function, solutions, adaptative)
			  if not s_ in tabu:
					  if len(tabu) == t:
							  tabu.popleft()
					  tabu.append(s_)
					  s_best = s_
					  f.write('%s \n' % str(s_best))
					  f.write('hit_rate: %s \n' % hit_rate)
	  
	return s_best
        
def __gen_neighbors_solutions(solution, m, n, p):
	
	solutions = list()
	
	for i in range(m*n):
			wx = random.uniform(-1, 1)
			fx = random.randint(0, len(solution[0])-1)
			kx = random.sample([1, 3, 5, 7, 9], 1)[0]
			#print 'wx', wx, 'fx', fx
			
			new_solution = (list(solution[0]), list(solution[1]), kx)
			new_solution[0][fx] = new_solution[0][fx] + wx
			
			#print 'sol', solution
			#print 'new', new_solution
			solutions.append(new_solution)
			
	for i in range(p):
			fx = random.randint(0, len(solution[1])-1)
			kx = random.randint(1, 5)
			
			#print 'fx', fx
			new_solution = (list(solution[0]), list(solution[1]), kx)
			if new_solution[1][fx]:
					new_solution[1][fx] = 0
			else:
					new_solution[1][fx] = 1
	
			#print 'sol', solution
			#print 'new', new_solution
			solutions.append(new_solution)
	
	#print len(solutions)
	return solutions
	
def __best_solution(training_set, test_set, knn_function, solutions, adaptative=False):
        
	best = (0, None)
	
	for s in solutions:
			#print training_set
			hit_rate = training_machine(training_set, test_set, knn_function, s, adaptative)
			if hit_rate > best[0]:
					best = (hit_rate, s)
	return best

if __name__ ==  '__main__':
  # Tabu search Adaptive
	"""
	solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
	processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
	(training_set, test_set) = process_data(processed_data, 70)
	
			  # Tabu search Adaptive

	with open('D:/CIn/logs/ts-adaptive.log','w') as f:
	
			print 'TS Adaptative Distance'
			best_solution = tabu_search(training_set, test_set, knn_euclidian, solution, 100, f, adaptative=True)
			f.write('best solution: %s' % str(best_solution))
			print 'Hits for the best solution'
			hits = training_machine(training_set, test_set, knn_euclidian, best_solution)
			f.write('Hits for the best solution: %s' % hits)
	
	
	solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
	processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
	(training_set, test_set) = process_data(processed_data, 70)
	with open('D:/CIn/logs/ts-euclidian.log','w') as f:
	# Tabu search Euclidian
			print 'TS Euclidian Distance'
			best_solution = tabu_search(training_set, test_set, knn_euclidian, solution, 100, f, adaptative=False)
			f.write('best solution: %s' % str(best_solution))
			print 'Hits for the best solution'
			hits = training_machine(training_set, test_set, knn_euclidian, best_solution)
			f.write('Hits for the best solution: %s' % hits)
	
	solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
	processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
	(training_set, test_set) = process_data(processed_data, 70)
	# Simulated Annealing Adaptive
	with open('D:/CIn/logs/sa-adaptive.log','w') as f:
			print 'SA Adaptative Distance'
			best_solution = simulated_annealing(training_set, test_set, knn_euclidian, solution, f, adaptative=True)
			f.write('best solution: %s' % str(best_solution))
			print 'Hits for the best solution'
			hits = training_machine(training_set, test_set, knn_euclidian, best_solution)
			f.write('Hits for the best solution: %s' % hits)
	
	solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
	processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
	(training_set, test_set) = process_data(processed_data, 70)
	# Simulated Annealing Euclidian
	with open('D:/CIn/logs/sa-euclidian.log','w') as f:
			print 'SA Euclidian Distance'
			best_solution = simulated_annealing(training_set, test_set, knn_euclidian, solution, f, adaptative=False)
			f.write('best solution: %s' % str(best_solution))
			print 'Hits for the best solution'
			hits = training_machine(training_set, test_set, knn_euclidian, best_solution)
			print hits
			f.write('Hits for the best solution: %s' % hits)
			
	
	# k-NN Euclidian
	list_qtde = []
	list_media = []
	media = 0.0
	best_k = (0,0)
	current_k = (0,0)
	for k in [1,3,5,7,9]:
			cur_media = 0.0
			for i in xrange(3):
					print 'k', k
					solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
					processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
					(training_set, test_set) = process_data(processed_data, 70)
					x = training_machine(training_set, test_set, knn_euclidian, ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],k), adaptative=True)
					print str(x)
					list_qtde.append(x)
					cur_media = cur_media + x
			current_k = (cur_media/3, k)
			list_media.append(cur_media/3)
			if current_k[0] >= best_k[0]:
					best_k = current_k
	print list_media
	print list_qtde
	print best_k
	"""
	# k-NN Euclidian
	list_qtde = []
	list_media = []
	media = 0.0
	best_k = (0,0)
	current_k = (0,0)
	for k in [1,3,5,7,9]:
			cur_media = 0.0
			for i in xrange(3):
					print 'k', k
					solution = ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],1)
					processed_data = get_liver_dataset('datasets/selected/heart-oss.data')
					(training_set, test_set) = process_data(processed_data, 70)
					x = training_machine(training_set, test_set, knn_euclidian, ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1],k))
					print str(x)
					list_qtde.append(x)
					cur_media = cur_media + x
			current_k = (cur_media/3, k)
			list_media.append(cur_media/3)
			if current_k[0] >= best_k[0]:
					best_k = current_k
	print list_media
	print list_qtde
	print best_k
	"""
	# Simulated Annealing
	#best_solution = simulated_annealing(training_set, test_set, knn_euclidian, solution, f, adaptative=True)
	#print 'Hits for the best solution'
	#print training_machine(training_set, test_set, knn_euclidian, best_solution)
	"""
