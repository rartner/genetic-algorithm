import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from individual import Individual

class Population():

    best_fit_plt    = []
    mean_fit_plt    = []
    diversity       = []
    coeficient      = 1.2
    max_diversity   = None
    best_individual = None

    def __init__(self, encoding, psize, csize, min_bound, max_bound, ctax, mtax, generations, is_bin, el, tsize = None):
        self.individuals = [Individual(csize, encoding, min_bound, max_bound) for i in range (0, psize)]
        self.generations = generations
        self.psize = psize
        self.csize = csize
        self.ctax = ctax
        self.mtax = mtax
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.encoding = encoding
        self.is_bin = is_bin
        self.has_elitism = el
        self.tsize = tsize
        self.adjustment = 0.8 / float(generations * 0.8)
        self.div = []
        self.avg = []

    def _diversity(self):
        ''' tks @markx3 '''
        chromos = np.array([ind.chromosome for ind in self.individuals])
        ci = np.sum(chromos, axis=0) / self.psize
        div = np.sum((chromos - ci) ** 2)
        self.diversity.append(div)

    def evolve(self):
        execution = 0
        while (execution < 1):
            generation = 0
            while(generation < self.generations):
                self._diversity()
                parents = self._select()
                self._crossover(parents)
                self._mutate()
                generation += 1
            self.div.append(self.diversity)
            self.avg.append(self.mean_fit_plt)
            self.diversity = []
            self.mean_fit_plt = []
            self.best_fit_plt = []
            execution += 1
        self.get_best_result()
        # self._plot()

    def _select(self):
        max_fitness = 0.0
        for i in self.individuals:
            i.eval_fitness()
            if (i.fitness > max_fitness):
                max_fitness = i.fitness
                if self.best_individual is None:
                    self.best_individual = deepcopy(i)
                if (i.fitness > self.best_individual.fitness):
                    self.best_individual = deepcopy(i)
        self.best_fit_plt += [max_fitness]
        sum_fitness = np.sum([i.fitness for i in self.individuals])
        self.mean_fit_plt += [float(sum_fitness) / self.psize]
        if self.tsize is not None:
            return self._tournment()
        else:
            return self._roulette()

    def _crossover(self, parents):
        mates = 0
        if (self.has_elitism):
            self.individuals[mates] = deepcopy(self.best_individual)
            self.best_individual
            mates += 1
        father, mother = None, None
        while (mates <= self.psize - 1):
            ctax = np.random.uniform(0, 1)
            individual = parents[np.random.randint(self.psize)]
            if (ctax > self.ctax):
                self.individuals[mates].chromosome = individual.chromosome
                mates += 1
            else:
                if father is None:
                    father = individual
                else:
                    mother = individual
                    childs = father.mate(mother)
                    for c in childs:
                        if (mates < self.psize):
                            self.individuals[mates].chromosome = c
                            mates += 1
                    father, mother = None, None

    def _mutate(self):
        c = 0
        if (self.has_elitism):
            for i in range(1, self.psize):
                self.individuals[i].mutate(self.mtax)
        else:
            for i in range(self.psize):
                self.individuals[i].mutate(self.mtax)

    def _roulette(self):
        """Roulette-based selector."""
        self.linear_adjustment()

        list_fitness = [i.fitness for i in self.individuals]
        sum_fitness = np.sum(list_fitness)
        list_fitness = list_fitness / sum_fitness
        indexes = np.random.choice(self.psize, self.psize, p=list_fitness)
        parents = [self.individuals[i] for i in indexes]
        return parents

    def _tournment(self):
        """Tournment selector."""
        winners = []
        for i in range(self.psize):
            gladiators = random.sample(self.individuals, self.tsize)
            sorted_gladiators = sorted(gladiators, key=lambda ind: ind.fitness)
            winners.append(sorted_gladiators[len(gladiators) - 1])
        return winners

    def _plot(self):
        # ''' Fig 1 - Fitness '''
        # plt.figure(1)
        # plt.ylabel('fitness')
        # plt.xlabel('generation')
        # plt.plot(self.best_fit_plt)
        # plt.plot(self.mean_fit_plt)

        # plt.figure(2)
        avg = np.sum(self.avg, axis=0) / len(self.avg)
        plt.plot(list(avg))
        plt.plot(list(np.std(self.avg, axis=0)))
        plt.ylabel('fitness')
        plt.xlabel('generation')
        plt.legend(['media', 'desvio padrao'])

        ''' Fig 2 - Diversidade '''
        plt.figure(3)
        # self.div = [(float(x) / max(self.div)) for x in self.div]
        max_div = max([max(x) for x in self.div])
        list_div = list(np.sum(self.div, axis=0) / max_div * len(self.div))
        plt.plot(list_div / max(list_div))
        # plt.plot(self.div)
        plt.ylabel('diversity')
        plt.xlabel('generation')

        plt.show()

    def get_best_result(self):
        best = sorted(self.individuals, key=lambda i: i.fitness, reverse=True)[0]
        best.eval_fitness()
        best.show_board()
        # if (hasattr(best, 'num_genes')):
        #     if (best.num_genes):
        #         print ('Best individual: {}'.format(best.get_result()))
        # else:
        #     print ('=====================\nBest individual:\n{}. \nFitness: {}'.format(str(best), best.fitness))
        #     if (best.problem == 'qp'):
        #         print ('Clashes: ', best.get_clashes())

    def linear_adjustment(self):
        sortd = sorted(self.individuals, key=lambda i: i.fitness)
        fitness_min = sortd[0].fitness
        fitness_max = sortd[len(sortd)-1].fitness
        fitness_avg = np.average([i.fitness for i in self.individuals])
        if (fitness_min > ((self.coeficient * fitness_avg) - fitness_max) / (self.coeficient - 1)):
            alpha = (fitness_avg * (self.coeficient - 1)) / (fitness_max - fitness_avg)
            beta = (fitness_avg * (fitness_max - self.coeficient * fitness_avg)) / (fitness_max - fitness_avg)
        else:
            alpha = fitness_avg / (fitness_avg - fitness_min)
            beta = (-fitness_min  * fitness_avg) / (fitness_avg - fitness_min)
        for individual in self.individuals:
            individual.fitness = max(0, (alpha * individual.fitness) + beta)
        if (self.coeficient <= 2.00):
            self.coeficient += self.adjustment

    def __str__(self):
        strn = ''
        for i in self.individuals:
            strn += str(i) + '\n'
        return strn
