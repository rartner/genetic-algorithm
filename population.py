import copy
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from individual import Individual

class Population():

    best_fit_plt    = []
    mean_fit_plt    = []
    diversity       = []
    max_diversity   = None
    best_individual = None

    def __init__(self, encoding, psize, csize, min_bound, max_bound, ctax, mtax, generations, bin, el, tsize = None):
        self.individuals = [Individual(csize, encoding, min_bound, max_bound) for i in range (0, psize)]
        self.generations = generations
        self.psize = psize
        self.csize = csize
        self.ctax = ctax
        self.mtax = mtax
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.encoding = encoding
        self.is_bin = bin
        self.has_elitism = el
        self.tsize = tsize

    def _diversity(self):
        centroid = [(np.sum((self.individuals[i].chromosome[j]) for i in range(self.psize)) / self.psize) for j in range(self.csize)]
        diversity = [(np.sum(((self.individuals[i].chromosome[j] - centroid[j])**2) for i in range(self.psize))) for j in range(self.csize)]
        self.diversity.append(np.sum(diversity))
        return self._normalize(np.sum(diversity))

    def _normalize(self, value):
        if (self.max_diversity):
            return (value / self.max_diversity)
        else:
            self.max_diversity = value
            return 1

    def evolve(self):
        generation = 0
        while(generation < self.generations):
            parents = self._select()
            self._crossover(parents)
            self._mutate()
            self._diversity()
            generation += 1
        self._plot()

    def _select(self):
        max_fitness = 0.0
        for i in self.individuals:
            i.eval_fitness()
            if (i.fitness > max_fitness):
                max_fitness = i.fitness
                if (self.best_individual == None):
                    self.best_individual = i
                if (i.fitness > self.best_individual.fitness):
                    self.best_individual = i
        self.best_fit_plt += [max_fitness]
        if (self.tsize != None):
            return self._tournment()
        else:
            return self._roulette()

    def _crossover(self, parents):
        for i in parents:
            i.ctax = np.random.RandomState().uniform(0, 1)
        mates = 0
        if (self.has_elitism):
            self.individuals[mates] = copy.deepcopy(self.best_individual)
            self.best_individual
            mates += 1
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
                        if (mates < self.psize):
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
        if (self.has_elitism):
            for i in range(1, self.psize):
                self.individuals[i].mutate(self.mtax)
        else:
            for i in range(self.psize):
                self.individuals[i].mutate(self.mtax)

    def _roulette(self):
        sum_fitness = np.sum([i.fitness for i in self.individuals])
        self.mean_fit_plt += [float(sum_fitness) / self.psize]
        for i in self.individuals:
            i.fitness = i.fitness / sum_fitness
            if (self.best_individual != None):
                if (i.fitness > self.best_individual.fitness):
                    self.best_individual = i
            else:
                self.best_individual = i
        indexes = np.random.choice(self.psize, self.psize, p=[i.fitness for i in self.individuals])
        parents = [self.individuals[i] for i in indexes]
        return parents

    def _tournment(self):
        return None

    def _plot(self):
        ''' Fig 1 - Fitness '''
        plt.figure(1)
        plt.plot(self.best_fit_plt)
        # best_x = np.linspace(0, self.generations - 1, self.generations * 10)
        # best_y = spline(range(self.generations), self.best_fit_plt, best_x)
        # plt.plot(best_x, best_y)

        plt.plot(self.mean_fit_plt)
        # mean_x = np.linspace(0, self.generations - 1, self.generations * 3)
        # mean_y = spline(range(self.generations), self.mean_fit_plt, mean_x)
        # plt.plot(mean_x, mean_y)
        plt.legend(['best', 'mean'])
        plt.ylabel('fitness')
        plt.xlabel('generation')


        ''' Fig 2 - Diversidade '''
        plt.figure(2)
        plt.plot(self.diversity)
        # div_x = np.linspace(0, self.generations - 1, self.generations * 10)
        # div_y = spline(range(self.generations), self.diversity, div_x)
        # plt.plot(div_x, div_y)

        plt.ylabel('diversity')
        plt.xlabel('generation')

        plt.show()

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
