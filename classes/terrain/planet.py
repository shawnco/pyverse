'''
The base class for Planet objects
Planets come in three forms: gas giant, rocky, and terran
Their type determines their size and color
'''
import pygame
from constants import *
from classes.network.transceivercollection import *

class Planet(pygame.sprite.Sprite):
    '''
    Create the planet object by giving its type and location
    '''
    def __init__(self, id, type, x, y):
        super(Planet, self).__init__()
        self.id = id
        self.max_crystal = PLANETS[type]['max_crystal']
        self.max_gas = PLANETS[type]['max_gas']
        self.max_metal = PLANETS[type]['max_metal']
        self.size = PLANETS[type]['size']
        self.species = ''
        self.transceivers = TransceiverCollection()
        self.transceivers.add_transceiver(Transceiver(x,y))
        self.type = type
        self.x = x
        self.y = y
        
        
    '''
    Retrieve a transceiver by ID 
    '''
    def get_transceiver(self, index):
        return self.transceivers.get_transceiver(index)
        
    '''
    Draw the planet on each update
    '''
    def update(self):
        pygame.draw.circle(screen, PLANETS[self.type]['color'], (self.x, self.y), PLANETS[self.type]['size'])
        self.transceivers.update()