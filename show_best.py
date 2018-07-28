import cv2
import helper
import numpy as np

def best(individual):
  print ('fitness:', individual.fitness)
  print ('chromosome:', individual.chromosome)

def maze_solution(individual):
  best(individual)
  actual_position = np.array([10, 1])
  last_position = np.array([10, 1])
  visited = [[10, 1]]
  good_movements = 0
  for gene in individual.chromosome:
    new_position = None
    possible_movements = helper.get_possible_movements(
      actual_position, last_position, visited
    )
    if len(possible_movements) > 0:
      movement = gene % len(possible_movements)
      new_position = actual_position + possible_movements[movement]
      if list(new_position) == list(visited[len(visited) - 1]):
        good_movements += 0.5
      else:
        good_movements += 1
      last_position = np.array(actual_position)
      actual_position = np.array(new_position)
      visited.append(list(actual_position))

  helper.maze_board = np.array(helper.maze_board, dtype=np.uint8)
  helper.maze_board[helper.maze_board == 1] = 255
  helper.maze_board[helper.maze_board == 2] = 200
  helper.maze_board[helper.maze_board == 3] = 200

  for position in visited:
    helper.maze_board[position[0], position[1]] = 125
  
  helper.maze_board = cv2.resize(
    helper.maze_board, (600, 600), interpolation=cv2.INTER_NEAREST
  )
  cv2.imshow("path found", helper.maze_board)
  cv2.waitKey(0)
  print("movements:", good_movements)

