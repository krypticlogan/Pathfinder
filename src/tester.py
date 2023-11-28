from const import *
from city import City 
from grid import Grid
import pygame
import numpy as np

# grid =np.array([[0 for col in range(COLS)] for row in range(ROWS)])

# gameGrid = grid.astype('O')

# for row in range(ROWS):
#     for col in range(COLS):
#         gameGrid[row,col] = City(row,col,WHITE)

# print(gameGrid)

gr = Grid()


grid = gr.grid
start = grid[0,17]
start.toggle()
end = grid[13,17]
end.toggle()
# print(grid)
gr.find_start()
gr.find_end()


print(grid)

use = grid.flatten()

open = np.array([])
closed = []

open = np.append(open, gr.start)
print(open)



while open.size > 0:
    for city in open:
        # print(gr.findParents(city))
        pass





    



    

