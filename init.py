import numpy as np
from individual import Individual


def bin(chromo_size, pop_size, lower_bound=0, upper_bound=2):
    chromos = []
    for ind in range(pop_size):
        chromos.append(np.random.randint(2, size=chromo_size))
    return [Individual(chromo) for chromo in chromos]


def int(chromo_size, pop_size, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(np.random.randint(lower_bound, upper_bound, size=100))
    return [Individual(chromo) for chromo in chromos]


def int_perm(chromo_size, pop_size, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(np.random.permutation(chromo_size))
    return [Individual(chromo) for chromo in chromos]


def real(chromo_size, pop_size, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(
            np.random.uniform(lower_bound, upper_bound, size=chromo_size)
        )
    return [Individual(chromo) for chromo in chromos]
