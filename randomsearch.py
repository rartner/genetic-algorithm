"""Random search algorithm for Queen's problem."""
import numpy as np


def execute(size, executions):
    """Execute the random search algorithm."""
    arr_fitness = []
    for e in range(executions):
        chromosome = np.permutation(size)
        fitness = eval_fitness(size, chromosome)
        arr_fitness.append(fitness)
    return arr_fitness


def eval_fitness(size, chromosome):
    """Function for evaluation the fitness of the random solution."""
    print (size, chromosome)
