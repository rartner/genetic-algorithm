import numpy as np
import matplotlib.pyplot as plt
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

    def _diversity(self):
        soma = (np.sum((np.sum(i.chromosome) for i in self.individuals)) / len(self.individuals)) / len(self.individuals[0].chromosome)
        for i in self.individuals:
            media = 0
            for g in i.chromosome:
                media += abs(g - soma)
            print (media / len(i.chromosome))

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
