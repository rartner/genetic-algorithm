import math
import numpy as np

class Individual_Bin:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.randint(2, size=size)

    def fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] != self.chromosome[gene + 1]:
                fitness_value += 1
        return fitness_value

    def __str__(self):
        return np.array2string(self.chromosome)
