"""Random search algorithm for Queens problem."""
import numpy as np
import fitness


def execute(size, executions=1000000):
    """Execute the random search algorithm."""
    best_solution = {"fitness": 0, "chromosome": None}
    for e in range(executions):
        chromosome = np.random.permutation(size)
        fitness_value = fitness.queens(size, chromosome)
        if (fitness_value > best_solution['fitness']):
            best_solution['fitness'] = fitness_value
            best_solution['chromosome'] = chromosome
    return best_solution
