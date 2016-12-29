'''
This is the base class for Star objects.
Stars come in three colors: red, yellow, and blue
They also come in three sizes: dwarf, main, and giant
Color and size is determined at generation
'''
from classes.terrain.planetcollection import *
import pygame
from constants import *

class Star(pygame.sprite.Sprite):
    '''
    Load a star into the program by giving its ID, size, and color
    '''
    def __init__(self, id, size, color, x, y):
        self.id = id
        self.size = size
        self.color = color
        #self.planets = PlanetCollection()
        self.x = x
        self.y = y
        
    '''
    Draw the star given its location and visual information
    '''
    def update(self):
        pygame.draw.circle(screen, COLORS[self.color], (self.x, self.y), SIZES[self.size])