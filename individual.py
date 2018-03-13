import abc
import numpy as np
import math

class Bin():
    def __init__(self, size):
        self.__init_chromosome(size)

    def __init_chromosome(self, size):
        print ("bin")
        return np.random.randint(2, size=size)

class Real():
    def __init__(self, size, minbound, maxbound):
        print ("real")
        super(Real, self).__init__(size, minbound, maxbound)
        # self.__init_chromosome(size, minbound, maxbound)

    def __init_chromosome(self, size, minbound, maxbound):
        return np.random.uniform(minbound, maxbound, size=size)

    # def fitness(self, chromosome):
    #     '''
    #     Ackley's function
    #     '''
    # 	firstSum = 0.0
    # 	secondSum = 0.0
    # 	for c in chromosome:
    # 		firstSum += c**2.0
    # 		secondSum += math.cos(2.0*math.pi*c)
    # 	n = float(len(chromosome))
    # 	return -20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e

class Int():
    def __init__(self, size, minbound, maxbound):
        print ("int")
        self.__init_chromosome(size, minbound, maxbound)

    def __init_chromosome(self, size, minbound, maxbound):
        return np.random.randint(minbound, maxbound, size=size)

class Perm():
    def __init__(self, size):
        print ("perm")
        self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)


class Individual(Bin, Int, Real, Perm):
    def __init__(self, size, encoding, minbound, maxbound):
        print (encoding)
        if encoding == 'BIN':
            super(Bin, self).__init__(size)
        elif encoding == 'INT':
            super(Int, self).__init__(size, minbound, maxbound)
        elif encoding == 'REAL':
            super(Real, self).__init__(size, minbound, maxbound)
        elif encoding == 'INT-PERM':
            super(Perm, self).__init__(size)
        else:
            raise Exception('Invalid encoding')

        # self.encoding = encoding
        # self.chromosome = self.__init_chromosome(size, encoding, minbound, maxbound)

    # def __init_chromosome(self, encoding, size, minbound, maxbound):
    #     if encoding == 'BIN':
    #         return np.random.RandomState().randint(2, size=size)
    #     elif encoding == 'INT':
    #         return np.random.RandomState().randint(minbound, maxbound, size=size)
    #     elif encoding == 'REAL':
    #         return np.random.uniform(minbound, maxbound, size=size)
    #     elif encoding == 'INT-PERM':
    #         return np.random.RandomState().permutation(size)
    #     else:
    #         raise Exception('Invalid encoding')

    # def fitness_real(self, chromosome):
    # 	'''
    #     Ackley's function
    #     '''
    # 	firstSum = 0.0
    # 	secondSum = 0.0
    # 	for c in chromosome:
    # 		firstSum += c**2.0
    # 		secondSum += math.cos(2.0*math.pi*c)
    # 	n = float(len(chromosome))
    # 	return -20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e

    # def __str__(self):
    #     return np.array2string(self.chromosome)
