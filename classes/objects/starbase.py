'''
A Starbase is basically a multifunctional router and shipyard in space
'''
import pygame
from classes.network.router import *
from classes.network.terminalcollection import *

class Starbase(pygame.sprite.Sprite, Router):
    '''
    Create the starbase by fetching its ID and location
    '''
    def __init__(self, id, x, y):
        # Call parent constructors
        super(Starbase, self).__init__()
#        super(pygame.sprite.Sprite, self).__init__(x,y)
#        super(Router, self).__init__()
        
        self.id = id
        self.x = x
        self.y = y
        self.current_range = 0
        self.max_range = 500
        self.terminals = TerminalCollection()
        
        # A starbase by default has 5 terminals
        for i in range(5):
            self.terminals.add_terminal(Terminal(i, "Terminal {}".format(i)))
        
        # The build queue for a starship
        self.build_queue = []
        
        # Cooldown for smoother transmission display
        self.current_cooldown = 0
        self.cooldown = 25
        
        super(Router, self).__init__()
        
    def update(self, neighbors):
        super(pygame.sprite.Sprite, self).update(neighbors)