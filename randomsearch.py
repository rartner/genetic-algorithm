"""Random search algorithm for Queen's problem."""
import numpy as np
import fitness


def execute(size, executions):
    """Execute the random search algorithm."""
    arr_fitness = []
    for e in range(executions):
        chromosome = np.random.permutation(size)
        fitness_value = fitness.queens(size, chromosome)
        arr_fitness.append(fitness_value)
    return arr_fitness
