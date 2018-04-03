import math
import numpy as np

class Individual_Real:
    def __init__(self, size, min_bound, max_bound):
        self.size = size
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.is_bin = True
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

    def fitness(self):
        if self.is_bin:
            return self._fitness(self._decode_genes())
        else:
            return self._fitness(self.chromosome)

    ''' Ackley's function'''
    def _fitness(self, values):
    	first_sum = 0.0
    	second_sum = 0.0
    	for gene in values:
    		first_sum += gene ** 2.0
    		second_sum += math.cos(2.0 * math.pi * gene)
    	n = float(self.size)
    	return -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20 + math.e

    def __str__(self):
        return np.array2string(self.chromosome)
