import math
from random import gauss
import numpy as np

class Individual_Real:
    def __init__(self, size, min_bound, max_bound):
        self.size = size
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.is_bin = False
        self.chromosome = self.__init_chromosome(size, min_bound, max_bound)

    def _decode(self, genes):
        genes = [(int(gene, 2)) for gene in genes]
        genes = [(self.__to_domain(i)) for i in genes]
        print ('genes ', str(genes))
        return genes

    def __to_domain(self, value):
        print (value)
        return float(self.lb_domain + ((self.ub_domain - self.lb_domain + 1) / ((2 ** self.gene_size) - 1)) * value)

    def __init_chromosome(self, size, min_bound, max_bound):
        if (self.is_bin): # Ackley binary
            self.gene_size = 13
            self.num_genes = 2
            self.lb_domain = -32
            self.ub_domain = 32
            self.decimals = 2
            return np.random.randint(0, 2, size=(self.gene_size * self.num_genes))
        else:
            return np.random.uniform(min_bound, max_bound, size=size)

    def _decode_genes(self):
        genes = []
        for gene in np.split(self.chromosome, self.num_genes):
            genes.append(''.join(map(str, gene)))
        genes = self._decode(genes)
        return genes

    def sigmoid(self, value):
        return 1.0 / (1 + math.exp(-value))

    def eval_fitness(self):
        if self.is_bin:
            self._fitness(self._decode_genes())
        else:
            self._fitness(self.chromosome)

    def mutate(self, mtax):
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if (prob < mtax):
                value = gauss(self.chromosome[gene], 1)
                if (value < self.min_bound):
                    value = self.min_bound
                if (value > self.max_bound):
                    value = self.max_bound
                self.chromosome[gene] = value

    ''' Ackley's function'''
    def _fitness(self, values):
    	first_sum = 0.0
    	second_sum = 0.0
    	for gene in values:
    		first_sum += gene ** 2.0
    		second_sum += math.cos(2.0 * math.pi * gene)
    	n = float(self.size)
    	self.fitness = -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20 + math.e

    def __str__(self):
        return np.array2string(self.chromosome)
