import numpy as np
from copy import deepcopy


class Population:
    def __init__(
        self,
        problem,
        num_generations,
        pop_size,
        chromo_size,
        crossover_tax,
        mutation_tax,
        lower_bound,
        upper_bound,
    ):
        self.description = problem["description"]
        self.encoding = problem["encoding"]
        self.eval_fitness = problem["fitness"]
        self.selection = problem["selection"]
        self.crossover = problem["crossover"]
        self.mutation = problem["mutation"]

        self.individuals = problem["init_population"](
            chromo_size, lower_bound, upper_bound
        )
        self.num_generations = num_generations
        self.pop_size = pop_size
        self.chromo_size = chromo_size
        self.crossover_tax = crossover_tax
        self.mutation_tax = mutation_tax

        self.diversity = []
        self.best_individual = None


    def evolve(self):
        generation = 0
        while generation < self.num_generations:
            self.get_diversity()
            self.get_fitness()
            parents = self.selection(
              self.individuals, self.pop_size, None
            )


    def get_diversity(self):
        chromos = np.array([ind.chromosome for ind in self.individuals])
        ci = np.sum(chromos, axis=0) / self.pop_size
        div = np.sum((chromos - ci) ** 2)
        self.diversity.append(div)


    def get_fitness(self):
      max_fitness = 0.0
      for ind in self.individuals:
        ind.fitness = self.eval_fitness(ind)
        if (ind.fitness > max_fitness):
            max_fitness = ind.fitness
            if self.best_individual is None:
                self.best_individual = deepcopy(ind)
            if (ind.fitness > self.best_individual.fitness):
                self.best_individual = deepcopy(ind)


    def select(self):
      pass


    
