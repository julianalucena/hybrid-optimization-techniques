#!/usr/bin/python
#-*- coding:utf-8 -*-

import random

"""
The manager responsible for processing the datasets
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def get_ionosphere_dataset(data_path):
	"""
	Get all Ionosphere data
	
	@type data_path: str
	@param data_path: The data path
	
	@rtype: dict
	@returns: All Ionosphere data
	"""
	
	
	instances = dict()
	
	with open(data_path) as f:
		for line in f:
			t = line.split(',')
			inst = list()
			try:	
				for i in range(34):
					inst.append(float(t[i]))
			
				inst.append(t[34].rstrip('\n'))
				inst_class = t[34].rstrip('\n')
				
				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]
					
			except ValueError:
				pass			
	return instances

def get_liver_dataset(data_path):
	"""
	Get all Liver data
	
	@type data_path: str
	@param data_path: The data path
	
	@rtype: dict
	@returns: All Liver data
	"""
	
	instances = dict()
	
	with open(data_path) as f:
		for line in f:
			t = line.split(',')
			inst = list()
			try:	
				for i in range(6):
					inst.append(float(t[i]))
					
				inst.append(t[6].rstrip('\n'))
				inst_class = t[6].rstrip('\n')
				
				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]
					
			except ValueError:
				pass

	return instances	
def get_pima_dataset(data_path):
	"""
	Get all Pima data
	
	@type data_path: str
	@param data_path: The data path
	
	@rtype: dict
	@returns: All Pima data
	"""
	
	instances = dict()
	
	with open(data_path) as f:
		for line in f:
			t = line.split(',')
			inst = list()
			try:	
				for i in range(8):
					inst.append(float(t[i]))
					
				inst.append(t[8].rstrip('\n'))
				inst_class = t[8].rstrip('\n')
				
				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]
					
			except ValueError:
				pass			
	return instances

def get_sonar_dataset(data_path):
	"""
	Get all Sonar data	
	
	@type data_path: str
	@param data_path: The data path
	
	@rtype: dict
	@returns: All Sonar data
	"""
	
	instances = dict()
	
	with open(data_path) as f:
		for line in f:
			t = line.split(',')
			inst = list()
			try:	
				for i in range(60):
					inst.append(float(t[i]))
					
				inst.append(t[60].rstrip('\n'))
				inst_class = t[60].rstrip('\n')
				
				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]

			except ValueError:
				pass			
	return instances
	
def get_heart_dataset(data_path):
	"""
	Get all Heart data	

	@type data_path: str
	@param data_path: The data path

	@rtype: dict
	@returns: All Heart data
	"""
	
	instances = dict()

	with open(data_path) as f:
		for line in f:
			t = line.split(' ')
			inst = list()
			try:	
				for i in range(13):
					inst.append(float(t[i]))

				inst.append(t[13].rstrip('\n'))
				inst_class = t[13].rstrip('\n')

				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]

			except ValueError:
				pass		

	return instances
	
def get_australian_dataset(data_path):
	"""
	Get all Heart data	

	@type data_path: str
	@param data_path: The data path

	@rtype: dict
	@returns: All Heart data
	"""

	instances = dict()

	with open(data_path) as f:
		for line in f:
			t = line.split(' ')
			inst = list()
			try:	
				for i in range(14):
					inst.append(float(t[i]))

				inst.append(t[14].rstrip('\n'))
				inst_class = t[14].rstrip('\n')

				if instances.has_key(inst_class):
					instances[inst_class].append(inst)
				else:
					instances[inst_class] = [inst]

			except ValueError:
				pass		

	return instances
	
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
			#training[c] = l[:training_quantity]
			
		test[c] = l	
		#test[c] = l[training_quantity:]
		
	return (training, test)	
	
if __name__ == '__main__':
	#print get_ionosphere_dataset('datasets/ionosphere/ionosphere.data')
	#print get_liver_dataset('datasets/liver/bupa.data')
	#print get_pima_dataset('datasets/pima/pima-indians-diabetes.data')
	print get_sonar_dataset('datasets/sonar/sonar.all-data')