'''
A Starbase is basically a multifunctional router and shipyard in space
'''
import pygame
from classes.network.router import *

class Starbase(pygame.sprite.Sprite, Router):
    '''
    Create the starbase by fetching its ID and location
    '''
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.current_range = 0
        self.max_range = 400
        
        # Cooldown for smoother transmission display
        self.current_cooldown = 0
        self.cooldown = 25
        
        super(Router, self).__init__()
        
    def update(self):
        super(pygame.sprite.Sprite, self).update()