import argparse
import numpy as np
from population import Population

def main():
    parser = argparse.ArgumentParser(description='Genetic algorithm')
    parser.add_argument('-min',   type=int, help='lower bound', default=0)
    parser.add_argument('-max',   type=int, help='upper bound', default=10)
    parser.add_argument('-ctax',  type=float, help='crossover tax', default=1.0)
    parser.add_argument('-mtax',  type=int, help='mutate tax', default=0.03)
    parser.add_argument('-csize', type=int, help='chromosome size', default=10)
    parser.add_argument('-tsize', type=int, help='tournment size (for tournment selection)')
    parser.add_argument('-enc',   help='chromosome encoding', choices=['BIN', 'INT', 'REAL', 'INT-PERM'], required=True)
    parser.add_argument('-psize', type=int, help='population size', default=10)
    parser.add_argument('-seed',  type=int, help='seed')
    parser.add_argument('-bin', help='use binary genotype (for real or int encodings)', action='store_true')
    args = parser.parse_args()

    if (args.seed):
        np.random.seed(args.seed)

    pop = Population(args.enc,
                     args.psize,
                     args.csize,
                     args.min,
                     args.max,
                     args.ctax,
                     args.mtax)
    print (str(pop))
    pop.fitness()

if __name__ == '__main__':
    main()
