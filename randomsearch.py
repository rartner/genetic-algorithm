"""Random search algorithm for Queens problem."""
import fitness
import matplotlib.pyplot as plt
import math
import numpy as np


def execute(size, executions=10):
    """Random search procedure."""
    best_solutions = []
    avg_solutions = []
    for ex in range(executions):
        result = random_search(size)
        best_solutions.append(result[0])
        avg_solutions.append(result[1])
    avg_solutions = np.sum(avg_solutions, axis=0) / len(avg_solutions)
    plot(avg_solutions, executions)
    gest_best_solution(best_solutions)


def random_search(size, generations=100000):
    """Execute the random search algorithm."""
    best_solution = {"fitness": 0, "chromosome": None}
    total_fitness = 0
    solutions = []
    for e in range(generations):
        chromosome = np.random.permutation(size)
        fitness_value = fitness.queens(size, chromosome)
        solutions.append(fitness_value)
        total_fitness += fitness_value
        if fitness_value > best_solution["fitness"]:
            best_solution["fitness"] = fitness_value
            best_solution["chromosome"] = chromosome
    return (best_solution, solutions)


def plot(avg_solutions, executions):
    """Plot fitness for the executions."""
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.plot(avg_solutions)
    plt.legend(["média"])
    plt.show()


def gest_best_solution(best_solutions):
    """Describe the best solution from random search."""
    best_solutions = sorted(best_solutions, key=lambda x: x["fitness"])
    best = best_solutions[len(best_solutions) - 1]
    print(best)
    get_clashes(best["chromosome"])


def get_clashes(solution):
    """Get the number of clashes on the solution."""
    clashes = 0
    gain = 0
    for i in range(len(solution)):
        for j in range(len(solution)):
            if i != j:
                dx = abs(i - j)
                dy = abs(solution[i] - solution[j])
                if dx == dy:
                    clashes += 1
        if i % 2 == 0:
            gain += math.sqrt((solution[i] + 1) + (i * len(solution)))
        else:
            gain += math.log10((solution[i] + 1) + (i * len(solution)))
    print("Gain:", gain)
    print("Clashes:", clashes)
