"""Collection of toy problems for testing the algorithm."""
import fitness

# TODO: create fitness, crossover and mutation lib

queens = {
    "description": "queens problem considering variable weights",
    "encoding": "int-perm",
    "fitness": fitness.queens,
    "crossover": None,
    "mutation": None
}

ackley = {
    "description": "ackley functions for N dimensions",
    "encoding": "real",
    "fitness": fitness.ackley,
    "crossover": None,
    "mutation": None
}

ackley_bin = {
    "description": "ackley functions for N dimensions using bin encoding",
    "encoding": "bin",
    "fitness": None,
    "crossover": None,
    "mutation": None
}

even_odd = {
    "description": "even/odd alternance",
    "encoding": "int",
    "fitness": fitness.even_odd,
    "crossover": None,
    "mutation": None
}
