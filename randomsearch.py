"""Random search algorithm for Queens problem."""
import fitness
import matplotlib.pyplot as plt
import numpy as np


def execute(size, executions=10):
    """Random search procedure."""
    best_solutions = []
    for ex in range(executions):
        best_solutions.append(random_search(size)['fitness'])
    plot(best_solutions, executions)


def random_search(size, generations=1000):
    """Execute the random search algorithm."""
    best_solution = {"fitness": 0, "chromosome": None}
    for e in range(generations):
        chromosome = np.random.permutation(size)
        fitness_value = fitness.queens(size, chromosome)
        if (fitness_value > best_solution['fitness']):
            best_solution['fitness'] = fitness_value
            best_solution['chromosome'] = chromosome
    return best_solution


def plot(solutions, executions):
    """Plot fitness for the executions."""
    plt.ylabel('fitness')
    plt.xlabel('generation')
    plt.plot(solutions)
