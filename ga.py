import argparse
import numpy as np
import sys, os
from population import Population

def main():
    parser = argparse.ArgumentParser(description='Genetic algorithm')

    ''' required arguments '''
    required = parser.add_argument_group('required arguments')
    required.add_argument('-generations', type=int, help='n of generations')
    required.add_argument('-enc',   help='chromosome encoding', choices=['BIN', 'INT', 'REAL', 'INT-PERM'])

    ''' optional arguments '''
    parser.add_argument('-min',   type=int, help='lower bound', default=0)
    parser.add_argument('-max',   type=int, help='upper bound', default=10)
    parser.add_argument('-ctax',  type=float, help='crossover tax', default=1.0)
    parser.add_argument('-mtax',  type=float, help='mutate tax', default=0.03)
    parser.add_argument('-csize', type=int, help='chromosome size', default=10)
    parser.add_argument('-tsize', type=int, help='tournment size (for tournment selection)')
    parser.add_argument('-psize', type=int, help='population size', default=10)
    parser.add_argument('-seed',  type=int, help='seed')
    parser.add_argument('-bin', help='use binary genotype (for real or int encodings)', action='store_true')
    parser.add_argument('-el', help='use elitism', action='store_true')

    args = parser.parse_args()

    if (args.seed):
        np.random.seed(args.seed)

    if (args.tsize < 2):
        raise Exception('O torneio deve possuir mais que 01 gladiador')

    pop = Population(args.enc,
                     args.psize,
                     args.csize,
                     args.min,
                     args.max,
                     args.ctax,
                     args.mtax,
                     args.generations,
                     args.bin,
                     args.el,
                     tsize=args.tsize)
    print ('first population:\n{}'.format(str(pop)))
    pop.evolve()
    print ('last population:\n{}'.format(str(pop)))

if __name__ == '__main__':
    main()
