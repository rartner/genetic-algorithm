"""Collection of toy problems for testing the algorithm."""
import fitness

# TODO: create fitness functions lib. use it

queens = {
    "description": "queens problem considering variable weights",
    "encoding": "int-perm",
    "fitness": fitness.queens
}

ackley = {
    "description": "ackley functions for N dimensions",
    "encoding": "real",
    "fitness": fitness.ackley
}

ackley_bin = {
    "description": "ackley functions for N dimensions using bin encoding",
    "encoding": "bin",
    "fitness": None  # TODO
}

even_odd = {
    "description": "even/odd alternance",
    "encoding": "int",
    "fitness": fitness.even_odd
}
