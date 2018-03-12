import numpy as np
import math
from individual import Individual

'''
Diversidade:
- centroid - bin/real
- hamming: bin
- euclidiana: real
- manhattan: inteiro
'''

class Population():
    def __init__(self, encoding, psize, csize, minbound, maxbound):
        self.individuals = [Individual(encoding, csize, minbound, maxbound) for i in range (0, psize)]
        self.psize = psize
        self.csize = csize
        self.minbound = minbound
        self.maxbound = maxbound
        self.encoding = encoding

    def _diversity(self):
        centroid = [(np.sum((self.individuals[i].chromosome[j]) for i in range(self.psize)) / self.psize) for j in range(self.csize)]
        diversity = [(np.sum(((self.individuals[i].chromosome[j] - centroid[j])**2) for i in range(self.psize))) for j in range(self.csize)]
        print (centroid)
        print (diversity)
        print (self.__sigmoid(np.sum(diversity)))

    def __sigmoid(self, diversity):
        return 1 / (1 + math.exp(-diversity))

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
