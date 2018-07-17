"""Collection of toy problems for testing the algorithm."""
import fitness, mutation, crossover, selection


queens = {
    "description": "queens problem considering variable weights",
    "encoding": "int-perm",
    "fitness": fitness.queens,
    "crossover": crossover.pmx,
    "mutation": mutation.inversion
}

ackley = {
    "description": "ackley functions for N dimensions",
    "encoding": "real",
    "fitness": fitness.ackley,
    "crossover": crossover.arithmetic,
    "mutation": mutation.delta
}

ackley_bin = {
    "description": "ackley functions for N dimensions using bin encoding",
    "encoding": "bin",
    "fitness": None,
    "crossover": crossover.uniform,
    "mutation": mutation.bitflip
}

even_odd = {
    "description": "even/odd alternance",
    "encoding": "int",
    "fitness": fitness.even_odd,
    "crossover": crossover.uniform,
    "mutation": mutation.randint
}

maze = {
    "description": "maze solver",
    "encoding": "int",
    "fitness": fitness.maze,
    "crossover": crossover.one_point,
    "mutation": mutation.randint
}
