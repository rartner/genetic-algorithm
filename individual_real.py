import math
import numpy as np
from copy import deepcopy
from random import gauss

class Individual_Real:
    def __init__(self, size, min_bound, max_bound):
        self.size = size
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.crossover = 'art'
        self.chromosome = self.__init_chromosome(size, min_bound, max_bound)

    def __init_chromosome(self, size, min_bound, max_bound):
        return np.random.uniform(min_bound, max_bound, size=size)

    def mate(self, mother):
        if (self.crossover == 'avg'):
            return self._avg(mother)
        elif (self.crossover == 'blx'):
            return self._blx(mother)
        else:
            return self._art(mother)

    def _avg(self, mother):
        ''' uniform average '''
        childs = [deepcopy(self.chromosome), deepcopy(mother.chromosome)]
        average = np.sum(np.array([self.chromosome, mother.chromosome]), axis=0) / 2
        for i in range(self.size):
            parent = np.random.randint(2)
            childs[parent][i] = average[i]
        return childs

    def _blx(self, mother):
        ''' blend crossover '''
        childs = [deepcopy(self.chromosome), deepcopy(mother.chromosome)]
        cross_dif = abs(childs[0] - childs[1])
        childs[0] = self.chromosome - (np.random.uniform(0,1) * cross_dif)
        childs[1] = mother.chromosome + (np.random.uniform(0,1) * cross_dif)
        return childs

    def _art(self, mother):
        ''' arithmetic crossover '''
        childs = [deepcopy(self.chromosome), deepcopy(mother.chromosome)]
        alpha = np.random.uniform(0, 1)
        childs[0] = (alpha * childs[0]) + ((1 - alpha) * childs[1])
        childs[1] = ((1 - alpha) * childs[0]) + (alpha * childs[1])
        return childs

    def _mutate(self, mtax):
        ''' delta mutation '''
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if (prob < mtax):
                value = np.random.uniform(self.min_bound, self.max_bound) / 10
                if (np.random.randint(2) == 0):
                    self.chromosome[gene] += value
                else:
                    self.chromosome[gene] -= value


    def mutate(self, mtax):
        ''' gaussian mutation '''
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if (prob < mtax):
                value = gauss(self.chromosome[gene], 1)
                if (value < self.min_bound):
                    value = self.min_bound
                if (value > self.max_bound):
                    value = self.max_bound
                self.chromosome[gene] = value

    ''' ackley function '''
    def eval_fitness(self):
        first_sum = 0.0
        second_sum = 0.0
        for gene in self.chromosome:
            first_sum += gene ** 2.0
            second_sum += math.cos(2.0 * math.pi * gene)
        n = float(self.size)
        self.fitness = 32 - (-20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20 + math.e)

    def __str__(self):
        return np.array2string(self.chromosome)
