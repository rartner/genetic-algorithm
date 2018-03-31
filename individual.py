import numpy as np
import math

class Individual_Bin:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.randint(2, size=size)

    def fitness(self):
        fitness_value = 0
        for gene in range(self.size - 1):
            if self.chromosome[gene] != self.chromosome[gene + 1]:
                fitness_value += 1
        return fitness_value

    def __str__(self):
        return np.array2string(self.chromosome)

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

class Individual_Real:
    def __init__(self, size, min_bound, max_bound):
        self.size = size
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.is_bin = True
        self.chromosome = self.__init_chromosome(size, min_bound, max_bound)
        self.conc()

    def _decode(self, value):
        value = int(str(value), 2)
        print ('value to decode:', value)
        return np.around( (self.lb_domain + (((self.ub_domain - self.lb_domain) / ((2 ** self.gene_size) - 1)  ) * value)), self.decimals)

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

    def conc(self):
        genes = []
        for gene in np.split(self.chromosome, self.num_genes):
            genes.append(''.join(map(str, gene)))
        genes_real = map(self._decode, genes)
        print ('>>>>>>>>>>>>>>>>>>>>>> individual')
        for i in genes_real:
            print ('value decoded:', i)

    ''' Ackley's function'''
    def fitness(self):
    	first_sum = 0.0
    	second_sum = 0.0
    	for gene in self.chromosome:
    		first_sum += gene ** 2.0
    		second_sum += math.cos(2.0 * math.pi * gene)
    	n = float(self.size)
    	return -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20 + math.e

    def __str__(self):
        return np.array2string(self.chromosome)

class Individual_Perm:
    def __init__(self, size):
        self.size = size
        self.chromosome = self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)

    def fitness(self):
        return 'fitness int-perm'

    def __str__(self):
        return np.array2string(self.chromosome)

class Individual():

    ''' Return the object according to the encoding '''
    def __new__(cls, size, encoding, min_bound, max_bound):
        if encoding == 'BIN':
            return Individual_Bin(size)
        elif encoding == 'INT':
            return Individual_Int(size, min_bound, max_bound)
        elif encoding == 'REAL':
            return Individual_Real(size, min_bound, max_bound)
        elif encoding == 'INT-PERM':
            return Individual_Perm(size)
        else:
            raise Exception('Invalid encoding')

    def sigmoid(self, value):
        return 1.0 / (1 + math.exp(-value))
