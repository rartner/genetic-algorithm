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
        print ('oi')

    def __str__(self):
        return np.array2string(self.chromosome)
