import math
import numpy as np

class Individual_Bin:
    def __init__(self, size):
        self.size = size
        self.mutate_uniform = False                     # crossover uniform
        self.cpoints = 1                                # crossover points
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.randint(2, size=size)

    def eval_fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] != self.chromosome[gene + 1]:
                fitness_value += 1
        self.fitness = fitness_value

    def mutate(self, mtax):
        for gene in range(self.size):
            prob = np.random.RandomState().uniform(0, 1)
            if (prob < mtax):
                # print ('Gene:', gene, '\tProb:', prob)
                self.chromosome[gene] = 0 if self.chromosome[gene] == 1 else 1

    def mate(self, mother):
        if (self.mutate_uniform):
            return self._uniform(mother)
        else:
            if (self.cpoints == 1):
                return self._one_point(mother)
            else:
                return self._two_points(mother)

    def _uniform(self, mother):
        childs = [[], []]
        for child in range(2):
            chromosome = np.zeros(len(self.chromosome), dtype=np.uint8)
            for i in range(len(self.chromosome)):
                if (np.random.randint(2) == 1):
                    chromosome[i] = self.chromosome[i]
                else:
                    chromosome[i] = mother.chromosome[i]
            childs[child] = chromosome
        return childs

    def _one_point(self, mother):
        childs = []
        idx = np.random.randint(1, self.size - 1)
        childs.append(self.chromosome[:idx] + mother.chromosome[idx:])
        childs.append(mother.chromosome[:idx] + self.chromosome[idx:])
        return childs

    def _two_points(self, mother):
        childs = []
        idx1 = np.random.randint(1, self.size - 1)
        idx2 = idx1
        while (idx2 == idx1):
            idx2 = np.random.randint(1, self.size - 1)
        if (idx1 > idx2): idx1, idx2 = idx2, idx1
        childs.append(self.chromosome[:idx] + mother.chromosome[idx:])
        childs.append(mother.chromosome[:idx] + self.chromosome[idx:])
        return childs

    def _sigmoid(self, value):
        return 1.0 / (1 + math.exp(-value))

    def __str__(self):
        return np.array2string(self.chromosome)
