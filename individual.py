import numpy as np

class Individual():
    def __init__(self, size, encoding, minbound, maxbound):
        self.encoding = encoding
        self.chromosome = self.__init_chromosome(size, encoding, minbound, maxbound)

    def __init_chromosome(self, encoding, size, minbound, maxbound):
        if encoding == 'BIN':
            return np.random.RandomState().randint(2, size=size)
        elif encoding == 'INT':
            return np.random.RandomState().randint(minbound, maxbound, size=size)
        elif encoding == 'REAL':
            return np.random.RandomState().uniform(minbound, maxbound, size=size)
        elif encoding == 'INT-PERM':
            return np.random.RandomState().permutation(size)
        else:
            raise Exception('Invalid encoding')

    def __str__(self):
        return np.array2string(self.chromosome)


'''
    WIP
'''

class Bin():
    def __init__(self, size):
        self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.randint(2, size=size)

class Real():
    def __init__(self, size, minbound, maxbound):
        self.__init_chromosome(size, minbound, maxbound)

    def __init_chromosome(self, size, minbound, maxbound):
        return np.random.uniform(minbound, maxbound, size=size)

class Int():
    def __init__(self, size, minbound, maxbound):
        self.__init_chromosome(size, minbound, maxbound)

    def __init_chromosome(self, size, minbound, maxbound):
        return np.random.randint(minbound, maxbound, size=size)

class Perm():
    def __init__(self, size):
        self.__init_chromosome(size)

    def __init_chromosome(self, size):
        return np.random.permutation(size)
