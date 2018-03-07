'''
    sudo pip install quantumrandom >> too slow
        import quantumrandom as qr
'''
import numpy as np

MIN_BOUND = 10
MAX_BOUND = 10

class Individual():
    def __init__(self, size, encoding):
        self.chromosome = self.init_chromosome(size, encoding)

    def init_chromosome(self, size, encoding):
        if encoding == "BIN":
            return np.random.randint(2, size=size)
        elif encoding == "INT":
            return np.random.randint(MIN_BOUND, MAX_BOUND, size=size)
        elif encoding == "REAL":
            return np.random.uniform(MIN_BOUND, MAX_BOUND, size=size)
        elif encoding == "PERM":
            return np.random.permutation(size)
        else:
            raise Exception("Invalid encoding")

    def __str__(self):
        return np.array2string(self.chromosome)

class Population(object):
    def __init__(self, popSize, chromosomeSize, encoding):
        self.individuals = [Individual(chromosomeSize, encoding) for i in range (0, popSize)]

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + "\n"
        return strn

def main():
    pop = Population(10, 10, "PERM")
    print (str(pop))

if __name__ == '__main__':
    main()

