import argparse
import numpy as np
from population import Population

def main():
    parser = argparse.ArgumentParser(description='Genetic algorithm')
    parser.add_argument('-min',   type=int, help='lower bound', default=0)
    parser.add_argument('-max',   type=int, help='upper bound', default=10)
    parser.add_argument('-csize', type=int, help='chromosome size', default=10)
    parser.add_argument('-enc',   help='chromosome encoding', choices= ['BIN', 'INT', 'REAL', 'INT-PERM'], required=True)
    parser.add_argument('-psize', type=int, help='population size', default=10)
    parser.add_argument('-seed',  type=int, help='seed')
    args = parser.parse_args()

    minbound = args.min if args.min else 0
    maxbound = args.max if args.max else 10
    csize = args.csize
    psize = args.psize
    if (args.seed):
        np.random.seed(args.seed)

    pop = Population(args.enc, psize, csize, minbound, maxbound)
    print (str(pop))

    pop._diversity()

if __name__ == '__main__':
    main()
