import numpy as np
import helper


def uniform(fst_parent, snd_parent):
    childs = [[], []]
    for child in range(2):
        chromosome = np.zeros(len(fst_parent), dtype=np.uint8)
        for i in range(len(fst_parent)):
            if np.random.randint(2) == 1:
                chromosome[i] = fst_parent[i]
            else:
                chromosome[i] = snd_parent[i]
        childs[child] = chromosome
    return childs


def one_point(fst_parent, snd_parent):
    childs = []
    idx = np.random.randint(1, len(fst_parent) - 1)
    childs.append(np.concatenate([fst_parent[:idx], snd_parent[idx:]]))
    childs.append(np.concatenate([snd_parent[:idx], fst_parent[idx:]]))
    return childs


def two_points(fst_parent, snd_parent):
    childs = []
    idx1 = np.random.randint(1, len(fst_parent) - 1)
    idx2 = idx1
    while idx2 == idx1:
        idx2 = np.random.randint(1, len(fst_parent) - 1)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    c1, c2 = list(fst_parent), list(snd_parent)
    c1[idx1:idx2] = snd_parent[idx1:idx2]
    c2[idx1:idx2] = fst_parent[idx1:idx2]
    childs.append(c1)
    childs.append(c2)
    return childs


def pmx(fst_parent, snd_parent):
    childs = []
    idx1 = np.random.randint(1, len(fst_parent) - 1)
    idx2 = idx1
    while idx2 == idx1:
        idx2 = np.random.randint(1, len(fst_parent) - 1)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    fst_child, snd_child = list(fst_parent), list(snd_parent)
    fst_child[idx1:idx2] = snd_parent[idx1:idx2]
    snd_child[idx1:idx2] = fst_parent[idx1:idx2]
    fst_child, snd_child = helper.pmx_order(fst_child, snd_child, idx1, idx2)
    childs.append(fst_child)
    childs.append(snd_child)
    return childs


def uniform_average(fst_parent, snd_parent):
    childs = [list(fst_parent), list(snd_parent)]
    average = np.sum(np.array([fst_parent, snd_parent]), axis=0) / 2
    for i in range(len(fst_parent)):
        parent = np.random.randint(2)
        childs[parent][i] = average[i]
    return childs


def blend(fst_parent, snd_parent):
    childs = [list(fst_parent), list(snd_parent)]
    cross_dif = abs(childs[0] - childs[1])
    childs[0] = fst_parent - (np.random.uniform(0, 1) * cross_dif)
    childs[1] = snd_parent + (np.random.uniform(0, 1) * cross_dif)
    return childs


def arithmetic(fst_parent, snd_parent):
    childs = [np.array(fst_parent), np.array(snd_parent)]
    alpha = np.random.uniform(0, 1)
    childs[0] = (alpha * childs[0]) + ((1 - alpha) * childs[1])
    childs[1] = ((1 - alpha) * childs[0]) + (alpha * childs[1])
    return [list(childs[0]), list(childs[1])]
