import copy
import cv2
import math
import numpy as np
from scipy.spatial.distance import euclidean


class Individual_Int:
    def __init__(self, size=100, min_bound=1, max_bound=5):
        self.size = 100
        self.min_bound = 1
        self.max_bound = 12
        self.crossover = "un"
        self.chromosome = self.__init_chromosome()
        self.board = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1,0,0],
                        [0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0],
                        [0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0],
                        [0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0],
                        [0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0],
                        [0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0],
                        [0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0],
                        [0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0],
                        [0,3,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0],
                        [0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0],
                        [0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0],
                        [0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0],
                        [0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],
                        [0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0],
                        [0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0],
                        [0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0],
                        [0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0],
                        [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0],
                        [0,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0],
                        [0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0],
                        [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0],
                        [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0],
                        [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0],
                        [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0],
                        [0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0],
                        [0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0],
                        [0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    def __init_chromosome(self):
        return np.random.randint(self.min_bound, self.max_bound, size=100)

    def eval_fitness(self):
        actual_position = np.array([10, 1])
        last_position = np.array([10, 1])
        visited = [[10, 1]]
        finish_position = np.array([1, 21])
        closest = [100, actual_position]
        good_movements = 0
        for gene in self.chromosome:
            new_position = None
            possible_movements = self.get_possible_movements(
                actual_position, last_position, visited
            )
            if (len(possible_movements) > 0):
                movement = gene % len(possible_movements)
                new_position = actual_position + possible_movements[movement]
                good_movements += 1
                last_position = np.array(actual_position)
                actual_position = np.array(new_position)
                visited.append(list(actual_position))
                dst = euclidean(actual_position, finish_position)
                if dst < closest[0]:
                    closest = [dst, actual_position]

        distance = euclidean(closest[1], finish_position) / 40
        # penalty = (wall_colisions / 80) + (bad_movements / 80)
        # self.fitness = max(0, (good_movements / 100) - penalty + distance * 0.8)
        # self.fitness = max(0, (good_movements / 100))
        self.fitness = max(0, (good_movements / 100) + distance * 0.8)

    def get_possible_movements(self, position, last_position, visited):
        """Get the number of possible movements in the position."""
        movements = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        possible_movements = []
        for movement in movements:
            new_position = np.array(position) + np.array(movement)
            if (
                self.board[new_position[0]][new_position[1]] == 1
                and list(new_position) not in visited
            ):
                if not (
                    new_position[0] >= 30
                    or new_position[0] < 0
                    or new_position[1] >= 25
                    or new_position[1] < 0
                ):
                    possible_movements.append(np.array(movement))
        return possible_movements

    def mutate(self, mtax):
        for gene in range(self.size):
            prob = np.random.uniform(0, 1)
            if prob < mtax:
                self.chromosome[gene] = np.random.randint(
                    self.min_bound, self.max_bound
                )

    def mate(self, mother):
        if self.crossover == "op":
            return self._one_point(mother)
        elif self.crossover == "tp":
            return self._two_points(mother)
        else:
            return self._uniform(mother)

    def _uniform(self, mother):
        childs = [[], []]
        for child in range(2):
            chromosome = np.zeros(len(self.chromosome), dtype=np.uint8)
            for i in range(len(self.chromosome)):
                if np.random.randint(2) == 1:
                    chromosome[i] = self.chromosome[i]
                else:
                    chromosome[i] = mother.chromosome[i]
            childs[child] = chromosome
        return childs

    def _one_point(self, mother):
        childs = []
        idx = np.random.randint(1, self.size - 1)
        childs.append(
            np.concatenate([self.chromosome[:idx], mother.chromosome[idx:]])
        )
        childs.append(
            np.concatenate([mother.chromosome[:idx], self.chromosome[idx:]])
        )
        return childs

    def _two_points(self, mother):
        childs = []
        idx1 = np.random.randint(1, self.size - 1)
        idx2 = idx1
        while idx2 == idx1:
            idx2 = np.random.randint(1, self.size - 1)
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        c1, c2 = (
            copy.deepcopy(self.chromosome),
            copy.deepcopy(mother.chromosome),
        )
        c1[idx1:idx2] = mother.chromosome[idx1:idx2]
        c2[idx1:idx2] = self.chromosome[idx1:idx2]
        childs.append(c1)
        childs.append(c2)
        return childs

    def show_board(self):
        actual_position = np.array([10, 1])
        last_position = np.array([10, 1])
        visited = [[10, 1]]
        good_movements = 0
        for gene in self.chromosome:
            new_position = None
            possible_movements = self.get_possible_movements(
                actual_position, last_position, visited
            )
            if len(possible_movements) > 0:
                movement = gene % len(possible_movements)
                new_position = actual_position + possible_movements[movement]
                good_movements += 1
                last_position = np.array(actual_position)
                actual_position = np.array(new_position)
                visited.append(list(actual_position))

        self.board = np.array(self.board, dtype=np.uint8)
        self.board[self.board == 1] = 255
        self.board[self.board == 2] = 200
        self.board[self.board == 3] = 200
        for position in visited:
            self.board[position[0], position[1]] = 125
        self.board = cv2.resize(
            self.board, (600, 600), interpolation=cv2.INTER_NEAREST
        )
        cv2.imshow("final", self.board)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("movimentos bons:", good_movements)

    def __str__(self):
        return np.array2string(self.chromosome)
