import numpy as np
import math
from individual import Individual

class Population():

    max_diversity = None

    def __init__(self, encoding, psize, csize, min_bound, max_bound):
        self.individuals = [Individual(csize, encoding, min_bound, max_bound) for i in range (0, psize)]
        self.psize = psize
        self.csize = csize
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.encoding = encoding

    def diversity(self):
        centroid = [(np.sum((self.individuals[i].chromosome[j]) for i in range(self.psize)) / self.psize) for j in range(self.csize)]
        diversity = [(np.sum(((self.individuals[i].chromosome[j] - centroid[j])**2) for i in range(self.psize))) for j in range(self.csize)]
        return self._normalize(np.sum(diversity))

    def _normalize(self, value):
        if (self.max_diversity):
            return (value / self.max_diversity)
        else:
            self.max_diversity = value
            return 1

    def fitness(self):
        for i in self.individuals:
            print (i.fitness(i.chromosome))

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
