"""Collection of toy problems for testing the algorithm."""
import fitness, mutation, crossover, selection, init, show_best


def get_problem(name):
    if name == "queens":
        return queens
    elif name == "ackley":
        return ackley
    elif name == "even_odd":
        return even_odd
    elif name == "maze":
        return maze
    else:
        raise Exception("Problem not found")


queens = {
    "description": "queens problem considering variable weights",
    "encoding": "int-perm",
    "init_population": init.int_perm,
    "fitness": fitness.queens,
    "crossover": crossover.pmx,
    "mutation": mutation.inversion,
    "show_best": show_best.best,
}

ackley = {
    "description": "ackley functions for N dimensions",
    "encoding": "real",
    "init_population": init.real,
    "fitness": fitness.ackley,
    "crossover": crossover.arithmetic,
    "mutation": mutation.delta,
    "selection": selection.roulette,
    "show_best": show_best.best,
}

ackley_bin = {
    "description": "ackley functions for N dimensions using bin encoding",
    "encoding": "bin",
    "init_population": init.bin,
    "fitness": None,
    "crossover": crossover.uniform,
    "mutation": mutation.bitflip,
    "show_best": show_best.best,
}

even_odd = {
    "description": "even/odd alternance",
    "encoding": "int",
    "init_population": init.int,
    "fitness": fitness.even_odd,
    "crossover": crossover.uniform,
    "mutation": mutation.randint,
    "show_best": show_best.best,
}

maze = {
    "description": "maze solver",
    "encoding": "int",
    "init_population": init.int,
    "fitness": fitness.maze,
    "crossover": crossover.one_point,
    "mutation": mutation.randint,
    "show_best": show_best.maze_solution,
}
