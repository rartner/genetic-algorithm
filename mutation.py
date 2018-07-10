"""Collection of mutation functions."""
import numpy as np

def randint(chromosome, mtax, lower_bound, upper_bound):
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if prob < mtax:
            chromosome[gene] = np.random.randint(
                lower_bound, upper_bound
            )