import numpy as np 


def bin(chromo_size, lower_bound=0, upper_bound=2):
  return np.random.randint(2, size=chromo_size)


def int(chromo_size, lower_bound=0, upper_bound=10):
  return np.random.randint(lower_bound, upper_bound, size=100)


def int_perm(chromo_size, lower_bound=0, upper_bound=10):
  return np.random.permutation(chromo_size)


def real(chromo_size, lower_bound=0, upper_bound=10):
  return np.random.uniform(lower_bound, upper_bound, size=chromo_size)
