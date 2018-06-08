'''
Melhor indivíduo para o TSP: [1 2 0 6 9 3 4 7 8 5]
Fitness: 96.50139350575246. Distância: ~~ 3.49
15k gerações / 5k gerações (às vezes)
'''
import time
import copy
import math
from random import uniform
import numpy as np
from scipy.spatial import distance

class Individual_Perm:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)
        self.problem = 'qp'
        self.points = [(0.0, 0.2), (0.15, 0.8), (0.2, 0.65), (0.9, 0.3), (0.75, 0.45), (0.3, 0.75), (0.05, 0.05), (0.95, 0.95), (0.55, 0.55), (0.85, 0.25)]
        self.distances = self._get_distances()

    def __init_chromosome(self, size):
        return np.random.permutation(size)

    def _get_distances(self):
        distances = np.zeros((len(self.points), len(self.points)), dtype=np.float)
        for y in range(len(self.points)):
            for x in range(len(self.points)):
                distances[y, x] = distance.euclidean(self.points[y], self.points[x])
        return distances

    def _fitness_qp(self):
        clashes = 0
        for i in range(self.size):
            for j in range(self.size):
                if (i != j):
                    dx = abs(i-j)
                    dy = abs(self.chromosome[i] - self.chromosome[j])
                    if(dx == dy):
                        clashes += 1
        self.fitness = (self.size ** 2) - clashes

    def _fitness_qp_weighted(self):
        clashes = 0
        weight = 0
        max_weight = 0
        weight_diagonal = [(x + 1) + (x * self.size) for x in range(self.size)]
        for x in range(self.size):
            if (x % 2 == 0):
                max_weight += math.sqrt(weight_diagonal[x])
            else:
                max_weight += math.log10(weight_diagonal[x])
        for i in range(self.size):
            for j in range(self.size):
                if (i != j):
                    dx = abs(i-j)
                    dy = abs(self.chromosome[i] - self.chromosome[j])
                    if(dx == dy):
                        clashes += 1
            gain = (self.chromosome[i] + 1) + (i * self.size)
            if (i % 2 == 0):
                gain = math.sqrt(gain)
            else:
                gain = math.log10(gain)
            weight += gain
        penalty = 1 - clashes / ((self.size - 1) ** 2)
        self.fitness = ((weight / max_weight) * penalty)

    def _fitness_tsp(self):
        soma = 0.0
        for i in range(1, self.size + 1):
            if (i == self.size):
                p1, p2 = self.chromosome[0], self.chromosome[i-1]
            else:
                p1, p2 = self.chromosome[i-1], self.chromosome[i]
            soma += self.distances[p2, p1]
        self.fitness = abs(100 - soma)

    def eval_fitness(self):
        if (self.problem == 'qp'):
            self._fitness_qp_weighted()
        else:
            self._fitness_tsp()

    def mutate(self, mtax):
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if (prob < mtax):
                pos = np.random.randint(0, self.size)
                aux = self.chromosome[pos]
                self.chromosome[pos] = self.chromosome[gene]
                self.chromosome[gene] = aux

    def mate(self, mother):
        childs = []
        idx1 = np.random.randint(1, self.size - 1)
        idx2 = idx1
        while (idx2 == idx1):
            idx2 = np.random.randint(1, self.size - 1)
        if (idx1 > idx2): idx1, idx2 = idx2, idx1
        c1, c2 = copy.deepcopy(self.chromosome), copy.deepcopy(mother.chromosome)
        c1[idx1:idx2] = mother.chromosome[idx1:idx2]
        c2[idx1:idx2] = self.chromosome[idx1:idx2]
        c1, c2 = self._pmx(c1, c2, idx1, idx2)
        childs.append(c1)
        childs.append(c2)
        return childs

    def _pmx(self, c1, c2, idx1, idx2):
        slice_1, slice_2 = c1[idx1:idx2], c2[idx1:idx2]
        for i in range(len(c1)):
            if (i < idx1 or i >= idx2):
                wait = True
                while (wait):
                    if (c1[i] in slice_1):
                        pos = list(slice_1).index(c1[i])
                        c1[i] = slice_2[pos]
                    if ((c1 == c1[i]).sum() > 1):
                        wait = True
                    else:
                        wait = False
        for i in range(len(c2)):
            if (i < idx1 or i >= idx2):
                wait = True
                while (wait):
                    if (c2[i] in slice_2):
                        pos = list(slice_2).index(c2[i])
                        c2[i] = slice_1[pos]
                    if ((c2 == c2[i]).sum() > 1):
                        wait = True
                    else:
                        wait = False
        return c1, c2

    def get_clashes(self):
        clashes = 0
        gain = 0
        for i in range(self.size):
            for j in range(self.size):
                if (i != j):
                    dx = abs(i-j)
                    dy = abs(self.chromosome[i] - self.chromosome[j])
                    if(dx == dy):
                        clashes += 1
            gain += (self.chromosome[i] + 1) + (i * self.size)
        print ('Gain: ', gain)
        return clashes

    def __str__(self):
        return np.array2string(self.chromosome)
