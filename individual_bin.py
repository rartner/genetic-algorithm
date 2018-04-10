import copy
import math
import numpy as np

class Individual_Bin:

    def __init__(self, size):
        self.size = size
        self.uniform_c = False # Uniform crossover
        self.cpoints = 1      # Crossover points
        self.rproblem = False
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        if (self.rproblem):
            self.gene_size = 5
            self.num_genes = 2
            return np.random.randint(0, 2, size=(self.gene_size * self.num_genes))
        else:
            return np.random.randint(2, size=size)

    def eval_fitness(self):
        if (self.rproblem):
            self._radio_fitness()
        else:
            self._bin_fitness()

    def _bin_fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] != self.chromosome[gene + 1]:
                fitness_value += 1
        self.fitness = fitness_value

    def mutate(self, mtax):
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if (prob < mtax):
                self.chromosome[gene] = 0 if self.chromosome[gene] == 1 else 1

    def mate(self, mother):
        if (self.uniform_c):
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
        childs.append(np.concatenate([self.chromosome[:idx], mother.chromosome[idx:]]))
        childs.append(np.concatenate([mother.chromosome[:idx], self.chromosome[idx:]]))
        return childs

    def _two_points(self, mother):
        childs = []
        idx1 = np.random.randint(1, self.size - 1)
        idx2 = idx1
        while (idx2 == idx1):
            idx2 = np.random.randint(1, self.size - 1)
        if (idx1 > idx2): idx1, idx2 = idx2, idx1
        c1, c2 = copy.deepcopy(self.chromosome), copy.deepcopy(mother.chromosome)
        c1[idx1:idx2] = mother.chromosome[idx1:idx2]
        c2[idx1:idx2] = self.chromosome[idx1:idx2]
        childs.append(c1)
        childs.append(c2)
        return childs

    def _sigmoid(self, value):
        return 1.0 / (1 + math.exp(-value))

    ''' Radios problem '''
    def _radio_fitness(self):
        genes = []
        for gene in np.split(self.chromosome, self.num_genes):
            genes.append(''.join(map(str, gene)))
        genes = self.decode(genes)
        fo = float((30*genes[0] + 40*genes[1]) / 1360)
        h = max(0, (genes[0] + 2*genes[1] - 40) / 16)
        self.fitness = fo - h

    def decode(self, genes):
        genes = [(int(gene, 2)) for gene in genes]
        genes[0] = int(( 24 / ((2 ** self.gene_size) - 1)) * genes[0] )
        genes[1] = int(( 16 / ((2 ** self.gene_size) - 1)) * genes[1] )
        return genes

    def get_result(self):
        genes = []
        for gene in np.split(self.chromosome, self.num_genes):
            genes.append(''.join(map(str, gene)))
        return str(self.decode(genes))

    def __str__(self):
        return np.array2string(self.chromosome)
