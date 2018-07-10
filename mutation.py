"""Collection of mutation functions."""
import numpy as np
from random import gauss


def randint(chromosome, mtax, lower_bound, upper_bound):
    """Generate a random integer number for the allele."""
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if prob < mtax:
            chromosome[gene] = np.random.randint(
                lower_bound, upper_bound
            )


def bitflip(chromosome, mtax, lower_bound=1, upper_bound=1):
    """Inverts the allele bit."""
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if (prob < mtax):
            chromosome[gene] = 0 if chromosome[gene] == 1 else 1


def inversion(chromosome, mtax, lower_bound=0, upper_bound=0):
    """Inverts two alleles values."""
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if (prob < mtax):
            pos = np.random.randint(0, len(chromosome))
            aux = chromosome[pos]
            chromosome[pos] = chromosome[gene]
            chromosome[gene] = aux


def delta(chromosome, mtax, lower_bound, upper_bound):
    """Delta mutation."""
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if (prob < mtax):
            value = np.random.uniform(lower_bound, upper_bound) / 10
            if (np.random.randint(2) == 0):
                chromosome[gene] += value
            else:
                chromosome[gene] -= value


def gaussian(chromosome, mtax, lower_bound, upper_bound):
    """Gaussian mutation."""
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if (prob < mtax):
            value = gauss(chromosome[gene], 1)
            if (value < lower_bound):
                value = upper_bound
            if (value > lower_bound):
                value = upper_bound
            chromosome[gene] = value