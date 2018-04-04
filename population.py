import numpy as np
import math
import time
from individual import Individual

class Population():

    max_diversity = None

    def __init__(self, encoding, psize, csize, min_bound, max_bound, ctax, mtax, tsize = None):
        self.individuals = [Individual(csize, encoding, min_bound, max_bound) for i in range (0, psize)]
        self.psize = psize
        self.csize = csize
        self.ctax = ctax
        self.mtax = mtax
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.encoding = encoding
        self.tsize = tsize

    def diversity(self):
        centroid = [(np.sum((self.individuals[i].chromosome[j]) for i in range(self.psize)) / self.psize) for j in range(self.csize)]
        diversity = [(np.sum(((self.individuals[i].chromosome[j] - centroid[j])**2) for i in range(self.psize))) for j in range(self.csize)]
        return self._normalize(np.sum(diversity))

    def _normalize(self, value):
        if (self.max_diversity):
            return (value / self.max_diversity)
        else:
            self.max_diversity = value
            return 1

    def fitness(self):
        generation = 0
        while(True):
            print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GERAÇÃO', generation, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            self.evolve()
            generation += 1
            # time.sleep(2)

    def evolve(self):
        print (' ==============  SELEÇÃO  ==============')
        parents = self._select()
        print (' ============== CROSSOVER ==============')
        self._crossover(parents)
        for i in self.individuals:
            print (str(i.chromosome))
        print (' ==============  MUTAÇÃO  ==============')
        self._mutate()
        for i in self.individuals:
            print (str(i.chromosome))

    def _select(self):
        for i in self.individuals:
            i.eval_fitness()
        if (self.tsize != None):
            return self._tournment()
        else:
            return self._roulette()

    def _crossover(self, parents):
        for i in parents:
            i.ctax = np.random.RandomState().uniform(0, 1)
        mates = 0
        father, mother = None, None
        while (mates <= self.psize - 1):
            individual = parents[np.random.randint(self.psize)]
            if (i.ctax > self.ctax):
                self.individuals[mates].chromosome = individual
                mates += 1
            else:
                if (father == None):
                    father = individual
                else:
                    mother = individual
                    childs = father.mate(mother)
                    for c in childs:
                        self.individuals[mates].chromosome = c
                        mates += 1
                    father, mother = None, None

    def _mate(self, father, mother, mates):
        for child in range(2):
            chromosome = np.zeros(self.csize)
            for i in range(self.csize):
                if (np.random.randint(2) == 1):
                    chromosome[i] = father.chromosome[i]
                else:
                    chromosome[i] = mother.chromosome[i]
            self.individuals[mates].chromosome = chromosome
            mates += 1

    def _mutate(self):
        c = 0
        for i in self.individuals:
            print ('> Indivíduo', c)
            i.mutate(self.mtax)
            c += 1

    def _roulette(self):
        sum_fitness = np.sum([i.fitness for i in self.individuals])
        print ('soma fitness: ', sum_fitness)
        fit = [i.fitness for i in self.individuals]
        for i in range(self.psize):
            if (fit[i] == 9):
                time.sleep(100)
        idx = 0
        for i in self.individuals:
            i.fitness = i.fitness / sum_fitness
            print (idx, i.fitness * sum_fitness, '\t', i.fitness)
            idx += 1
        indexes = np.random.choice(self.psize, self.psize, p=[i.fitness for i in self.individuals])
        print ('indexes selecionados: ', indexes)
        parents = [self.individuals[i] for i in indexes]
        return parents

    def _tournment(self):
        return None

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
