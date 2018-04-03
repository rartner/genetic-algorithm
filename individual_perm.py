import math
import numpy as np

class Individual_Perm:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)

    def fitness(self):
        return 'fitness int-perm'

    def __str__(self):
        return np.array2string(self.chromosome)
