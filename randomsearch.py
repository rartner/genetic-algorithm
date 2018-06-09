"""Random search algorithm for Queen's problem."""
import math
import numpy as np


def execute(size, executions):
    """Execute the random search algorithm."""
    arr_fitness = []
    for e in range(executions):
        chromosome = np.random.permutation(size)
        fitness = eval_fitness(size, chromosome)
        arr_fitness.append(fitness)
    return arr_fitness


def eval_fitness(size, chromosome):
    """Function for evaluating the fitness of the random solution."""
    clashes = 0
    weight = 0
    max_weight = 0
    weight_diagonal = [(x + 1) + (x * size) for x in range(size)]
    for i in range(size):
        if (i % 2 == 0):
            max_weight += math.sqrt(weight_diagonal[i])
        else:
            max_weight += math.log10(weight_diagonal[i])

        for j in range(size):
            if (i != j):
                dx = abs(i-j)
                dy = abs(chromosome[i] - chromosome[j])
                if(dx == dy):
                    clashes += 1
        gain = (chromosome[i] + 1) + (i * size)
        if (i % 2 == 0):
            gain = math.sqrt(gain)
        else:
            gain = math.log10(gain)
        weight += gain
    penalty = 1 - clashes / ((size) ** 2)
    return ((weight / max_weight) * penalty)
