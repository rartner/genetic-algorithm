import numpy as np
import random

def roulette(individuals, pop_size, tournment_size=0):
  list_fitness = [ind.fitness for ind in individuals]
  sum_fitness = np.sum(list_fitness)
  list_fitness = list_fitness / sum_fitness
  indexes = np.random.choice(pop_size, pop_size, p=list_fitness)
  parents = [individuals[i] for i in indexes]
  return parents


def tournment(individuals, pop_size, tournment_size):
  winners = []
  for i in range(pop_size):
      gladiators = random.sample(individuals, tournment_size)
      sorted_gladiators = sorted(gladiators, key=lambda ind: ind.fitness)
      winners.append(sorted_gladiators[tournment_size - 1])
  return winners
