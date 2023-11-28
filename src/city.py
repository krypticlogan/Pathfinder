from const import *
import const
import pygame


class City:
    
    PADDING = 15

    def __init__(self, row, col, color):
        self.g = 0
        self.h = 0
        self.f = 0
        self.row = row
        self.col = col
        self.enroute = False
        self.color = color
        self.start = False
        self.end = False
        self.selected = False
        self.x = 0
        self.y = 0
        self.calc_coords()
        self.index = self.row * ROWS + self.col


    def draw(self, screen):
        length = SQSIZE - self.PADDING
        rect = pygame.Rect(self.x+5, self.y+5, length, length)
        pygame.draw.rect(screen, self.color, rect)

    def calc_coords(self):
        self.x = self.col * SQSIZE
        self.y = self.row * SQSIZE

    def findF(self):
        if self.start:
            self.f = 0
        else:
            self.f = self.h + self.g


    def toggle(self):
        if self.selected == False:
            self.color = BLUE
            self.enroute = True
            self.selected = True

            if const.num_selected == 0:
                self.start = True

            if const.num_selected == 1:
                self.end = True

            const.num_selected+=1
        else: 
            self.color = WHITE
            self.enroute = False
            self.selected = False
            self.num_selected-=1
    
        
    def __repr__(self):
        if self.start:
            return str('S')
        if self.end:
            return str('E')
        if self.enroute:
            return str('Y')
        else: 
            return str('N')


    # def __repr__(self):
    #     return str(self.index)