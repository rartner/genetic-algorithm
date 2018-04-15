import time
import copy
import math
import numpy as np

class Individual_Perm:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)

    def eval_fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] % 2 == 0:
                if self.chromosome[gene + 1] % 2 == 1:
                    fitness_value += 1
            else:
                if self.chromosome[gene + 1] % 2 == 0:
                    fitness_value += 1
        self.fitness = fitness_value

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

    def __str__(self):
        return np.array2string(self.chromosome)
