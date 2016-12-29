'''
A relay is a purely routing object. It simply transfers packets from one point to another.
'''

import pygame
from classes.network.router import *

class Relay(pygame.sprite.Sprite, Router):
    '''
    Create the router by fecthing its ID and coordinates
    '''
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.current_range = 0
        self.max_range = 500
        self.current_cooldown = 0
        self.cooldown = 25
        super(Router, self).__init__()
        
    '''
    Display the relay
    '''
    def update(self):
        super(pygame.sprite.Sprite, self).update()