import math
import numpy as np

class Individual_Int:
    def __init__(self, size, min_bound, max_bound):
        self.size = size
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.is_bin = True
        self.chromosome = self.__init_chromosome(size, min_bound, max_bound)

    def __init_chromosome(self, size, min_bound, max_bound):
        if (self.is_bin): # radios
            self.gene_size = 5
            self.num_genes = 2
            return np.random.randint(0, 2, size=(self.gene_size * self.num_genes))
        else:
            return np.random.randint(min_bound, max_bound, size=size)

    def fitness(self):
        if(self.is_bin):
            return self._bin_fitness()
        else:
            return self._original_fitness()

    def _decode(self, genes):
        genes = [(int(gene, 2)) for gene in genes]
        genes[0] = int(( 24 / ((2 ** self.gene_size) - 1)) * genes[0] )
        genes[1] = int(( 16 / ((2 ** self.gene_size) - 1)) * genes[1] )
        return genes

    def _bin_fitness(self):
        genes = []
        for gene in np.split(self.chromosome, self.num_genes):
            genes.append(''.join(map(str, gene)))
        genes = self._decode(genes)
        fo = float((30*genes[0] + 40*genes[1]) / 1360)
        h = max(0, (genes[0] + 2*genes[1] - 40) / 16)
        print (fo - h)
        return fo - h

    def _original_fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] % 2 == 0:
                if self.chromosome[gene + 1] % 2 == 1:
                    fitness_value += 1
            else:
                if self.chromosome[gene + 1] % 2 == 0:
                    fitness_value += 1
        return fitness_value

    def __str__(self):
        return np.array2string(self.chromosome)
