import argparse
import numpy as np
import problems
from population import Population


def main():
    parser = argparse.ArgumentParser(description="Genetic algorithm")

    """ required arguments """
    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "-problem",
        help="name of the problem at the problems.py module",
        required=True,
        choices=["maze", "even_odd", "ackley", "queens"],
    )
    required.add_argument(
        "-gen", type=int, help="n of generations", required=True
    )

    """ optional arguments """
    parser.add_argument("-lb", type=int, help="lower bound", default=0)
    parser.add_argument("-ub", type=int, help="upper bound", default=10)
    parser.add_argument("-ctax", type=float, help="crossover tax", default=0.8)
    parser.add_argument("-mtax", type=float, help="mutate tax", default=0.03)
    parser.add_argument("-csize", type=int, help="chromosome size", default=10)
    parser.add_argument(
        "-tsize", type=int, help="tournment size (for tournment selection)"
    )
    parser.add_argument("-psize", type=int, help="population size", default=10)

    args = parser.parse_args()
    problem = problems.get_problem(args.problem)

    pop = Population(
        problem,
        args.gen,
        args.psize,
        args.csize,
        args.ctax,
        args.mtax,
        args.lb,
        args.ub,
        args.tsize,
    )
    pop.evolve()


if __name__ == "__main__":
    main()
