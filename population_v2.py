import numpy as np
from copy import deepcopy
from individual import Individual


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
        self.select = problem["selection"]
        self.mate = problem["crossover"]
        self.mutate = problem["mutation"]

        self.individuals = problem["init_population"](
            chromo_size, pop_size, lower_bound, upper_bound
        )
        self.num_generations = num_generations
        self.pop_size = pop_size
        self.chromo_size = chromo_size
        self.crossover_tax = crossover_tax
        self.mutation_tax = mutation_tax
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.diversity = []
        self.best_individual = None


    def evolve(self):
        generation = 0
        while generation < self.num_generations:
            self.get_diversity()
            self.get_fitness(self.individuals)
            parents = self.select(
              self.individuals, self.pop_size, None
            )
            next_generation = self.crossover(parents)
            self.mutation(next_generation)
            self.individuals = next_generation
            generation += 1


    def get_diversity(self):
        chromos = np.array([ind.chromosome for ind in self.individuals])
        ci = np.sum(chromos, axis=0) / self.pop_size
        div = np.sum((chromos - ci) ** 2)
        self.diversity.append(div)


    def get_fitness(self, individuals):
      max_fitness = 0.0
      for ind in individuals:
        ind.fitness = self.eval_fitness(self.chromo_size, ind.chromosome)
        if ind.fitness > max_fitness:
          max_fitness = ind.fitness
          if self.best_individual is None:
            self.best_individual = deepcopy(ind)
          if ind.fitness > self.best_individual.fitness:
            self.best_individual = deepcopy(ind)


    def crossover(self, parents):
      next_generation = []
      for ind in range(0, self.pop_size, 2):
        ctax = np.random.uniform(0, 1)
        if ctax < self.crossover_tax:
          childs = self.mate(parents[ind].chromosome,
                             parents[ind + 1].chromosome)
          next_generation.append(Individual(childs[0]))
          next_generation.append(Individual(childs[1]))
        else:
          next_generation.append(Individual(parents[ind]))
          next_generation.append(Individual(parents[ind + 1]))
      self.get_fitness(next_generation)
      next_generation = sorted(next_generation, key=lambda ind: ind.fitness)
      next_generation[0] = deepcopy(self.best_individual)
      return next_generation


    def mutation(self, individuals):
      for ind in individuals:
        self.mutate(
          ind.chromosome, self.mutation_tax, self.lower_bound, self.upper_bound
        )




    
