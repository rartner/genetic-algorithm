"""Module containing the fitness functions for the toy problems."""
import helper
import math
import numpy as np
from scipy.spatial.distance import cityblock


def queens(size, chromosome):
    """Fitness for the queens problem."""
    clashes = 0
    weight = 0
    max_weight = 0
    weight_diagonal = [(x + 1) + (x * size) for x in range(size)]
    for i in range(size):
        if i % 2 == 0:
            max_weight += math.sqrt(weight_diagonal[i])
        else:
            max_weight += math.log10(weight_diagonal[i])

        for j in range(size):
            if i != j:
                dx = abs(i - j)
                dy = abs(chromosome[i] - chromosome[j])
                if dx == dy:
                    clashes += 1
        gain = (chromosome[i] + 1) + (i * size)
        if i % 2 == 0:
            gain = math.sqrt(gain)
        else:
            gain = math.log10(gain)
        weight += gain
    penalty = 1 - clashes / ((size) ** 2)
    return (weight / max_weight) * penalty


def ackley(size, chromosome):
    first_sum = 0.0
    second_sum = 0.0
    for gene in chromosome:
        first_sum += gene ** 2.0
        second_sum += math.cos(2.0 * math.pi * gene)
    n = float(size)
    fst = -20.0 * math.exp(-0.2 * math.sqrt(first_sum / n))
    snd = math.exp(second_sum / n) + 20 + math.e
    return 32 - (fst - snd)


def even_odd(size, chromosome):
    """Even/odd alternance problem. <-- useless -->."""
    fitness_value = 0
    for gene in range(size - 1):
        if chromosome[gene] % 2 == 0:
            if chromosome[gene + 1] % 2 == 1:
                fitness_value += 1
        else:
            if chromosome[gene + 1] % 2 == 0:
                fitness_value += 1
    return fitness_value


def maze(size, chromosome):
    actual_position = np.array([10, 1])
    last_position = np.array([10, 1])
    visited = [[10, 1]]
    finish_position = np.array([1, 21])
    closest = [100, actual_position]
    for gene in chromosome:
        new_position = None
        possible_movements = helper.get_possible_movements(
            actual_position, last_position, visited
        )
        if len(possible_movements) > 0:
            movement = gene % len(possible_movements)
            new_position = actual_position + possible_movements[movement]
            last_position = np.array(actual_position)
            actual_position = np.array(new_position)
            visited.append(list(actual_position))
            dst = cityblock(actual_position, finish_position) / 40
            if dst < closest[0]:
                closest = [dst, actual_position]
    distance = cityblock(closest[1], finish_position) / 55
    return 1 - distance
