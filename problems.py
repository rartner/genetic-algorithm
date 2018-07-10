"""Collection of toy problems for testing the algorithm."""
import fitness, mutation, crossover, selection

# TODO: create fitness, crossover and mutation lib

queens = {
    "description": "queens problem considering variable weights",
    "encoding": "int-perm",
    "fitness": fitness.queens,
    "crossover": None,
    "mutation": mutation.inversion
}

ackley = {
    "description": "ackley functions for N dimensions",
    "encoding": "real",
    "fitness": fitness.ackley,
    "crossover": None,
    "mutation": mutation.delta
}

ackley_bin = {
    "description": "ackley functions for N dimensions using bin encoding",
    "encoding": "bin",
    "fitness": None,
    "crossover": None,
    "mutation": mutation.bitflip
}

even_odd = {
    "description": "even/odd alternance",
    "encoding": "int",
    "fitness": fitness.even_odd,
    "crossover": None,
    "mutation": mutation.randint
}

maze = {
    "description": "maze solver",
    "encoding": "int",
    "fitness": fitness.maze,
    "crossover": None,
    "mutation": mutation.randint
}
