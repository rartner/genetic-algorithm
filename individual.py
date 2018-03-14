import abc
import numpy as np
import math

class Bin:
    def __init__(self, size):
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.randint(2, size=size)

    def fitness(self, chromosome):
        return 'fitness bin'

    def __str__(self):
        return np.array2string(self.chromosome)

class Int:
    def __init__(self, size, min_bound, max_bound):
        self.__init_chromosome(size, min_bound, max_bound)

    def __init_chromosome(self, size, min_bound, max_bound):
        return np.random.randint(min_bound, max_bound, size=size)

    def fitness(self, chromosome):
        return 'fitness int'

    def __str__(self):
        return np.array2string(self.chromosome)

class Real:
    def __init__(self, size, min_bound, max_bound):
        self.chromosome = self.__init_chromosome(size, min_bound, max_bound)

    def __init_chromosome(self, size, min_bound, max_bound):
        return np.random.uniform(min_bound, max_bound, size=size)

    ''' Ackley's function '''
    def fitness(self, chromosome):
    	firstSum = 0.0
    	secondSum = 0.0
    	for c in chromosome:
    		firstSum += c**2.0
    		secondSum += math.cos(2.0*math.pi*c)
    	n = float(len(chromosome))
    	return -20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e

    def __str__(self):
        return np.array2string(self.chromosome)

class Perm:
    def __init__(self, size):
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)

    def fitness(self, chromosome):
        return 'fitness int-perm'

    def __str__(self):
        return np.array2string(self.chromosome)

class Individual():

    ''' Return the object according to the encoding '''
    def __new__(cls, size, encoding, min_bound, max_bound):
        if encoding == 'BIN':
            return Bin(size)
        elif encoding == 'INT':
            return Int(size, min_bound, max_bound)
        elif encoding == 'REAL':
            return Real(size, min_bound, max_bound)
        elif encoding == 'INT-PERM':
            return Perm(size)
        else:
            raise Exception('Invalid encoding')
