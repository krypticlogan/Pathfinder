from const import *
import numpy as np
from city import City
import pygame
import math

class Grid:
    def __init__(self):
        self.grid =np.array([[City(row,col,WHITE) for col in range(COLS)] for row in range(ROWS)])
        self.start =  None
        self.end = None
        self.route = []


    def drawSquares(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE - 5, SQSIZE - 5)
                pygame.draw.rect(surface, GRAY, rect)

    def draw(self, screen):
        self.drawSquares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                city = self.grid[row][col]
                city.draw(screen)

    def changeGrid(self):
        for row in range(ROWS):
            for col in range(COLS):
                place = self.grid[row,col]
                if place.enroute:
                    place.color = BLUE
                

    def getCity(self,row,col):
        city = self.grid[row,col]
        return city
    
    # def checkStart(self,row,col):
    #     for i in range(ROWS):
    #         for j in range(COLS):
    #             place = self.grid[i,j]
    #             if place.start:
    #                 self.grid[row,col].end = True
    #             else:
    #                 self.grid[row,col].start = True

                # self.grid[row,col] = 


    def find_start(self):
        for row in range (ROWS):
            for col in range (COLS):
                city = self.getCity(row,col)
                if city.start:
                    self.start = row, col
                

    def find_end(self):
         for row in range (ROWS):
            for col in range (COLS):
                city = self.grid[row,col]
                if city.end:
                    self.end = row,col

    def find_route(self):
        for row in range(ROWS):
            for col in range(COLS):
                city = self.getCity(row,col)
                if city.enroute:
                    self.route.append((row, col))


    def findH(self, row, col):
        city = self.getCity(row,col)
        end_row, end_col = self.end
        dist = math.sqrt((end_row - row)**2+(end_col - col)**2)
        city.h = dist

    def findG(self, row, col):
        city = self.getCity(row,col)
        start_row, start_col = self.start
        man_dist = abs(row - start_row) + abs(col - start_col)
        city.g = man_dist


    def findParents(self,city):
        row = city.row
        col = city.col

        if(row == 0 or col == 0 or col == COLS-1 or row == ROWS-1):
            # if(row == 0) and (col == 0):
            #     self.parents = self.grid[row: row +2,col: col+2]
            #     self.parents = np.array(self.parents).flatten()
            #     self.parents = np.delete(self.parents, 0)
                
            # elif(col == COLS):
            #     self.parents = self.grid[row: row +2, col-2: col]
            #     self.parents = np.array(self.parents).flatten()
            #     self.parents = np.delete(self.parents, 1)

            # else:
            #     self.parents = self.grid[row-1: row +2]
            #     self.parents = np.array(self.parents).flatten()
            #     # self.parents = np.delete(self.parents, 4)
            if(row == 0):
                startRow = row
                endRow = row + 2
            elif(row == ROWS-1):
                startRow = row - 1
                endRow = row+1
            else:
                startRow = row - 1
                endRow = row +2
            
            if(col == 0):
                startCol = col
                endCol = col + 2
            elif(col == COLS -1):
                endCol = col+1
                startCol = col-1
            else:
                startCol = col -1
                endCol = col + 2


            self.parents = np.array(self.grid[startRow : endRow, startCol : endCol])
            i = 0
            for row in self.parents:
                for parent in row:
                    if parent.start:
                        print(parent)
                        self.parents = np.delete(self.parents, i)
                    i+=1
            
        else:
            self.parents = self.grid[row-1: row+2, col-1: col+2]
            self.parents = np.array(self.parents).flatten()
            self.parents = np.delete(self.parents, 4)

        return self.parents
    



        

g = Grid()
grid = g.grid

start = grid[0,19]
start.toggle()
g.find_start()

print(grid)
print(g.findParents(start))
