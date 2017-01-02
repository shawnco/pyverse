'''
The grid divides the galaxy fields into discrete units. This is for discovering and location neighbor objects.
'''
import math
from constants import *

class Grid:
    '''
    Take the galaxy size and divide it into appropriately-sized unit squares
    '''
    def __init__(self, width, height):
        '''
        The grid itself is a dictionary of tuples. It stores the location of the following types of objects:
        * Planets
        * Stars
        * Starbases
        * Stations
        * Starships
        
        Each dictionary entry is just a list of the specified object.
        '''
        self.grid = {}
        
        # Get the rows and cols of the grid
        rows = math.ceil(width/CELL)
        cols = math.ceil(height/CELL)
        mid = CELL/2
        
        # Create the grid
        for r in range(rows):
            for c in range(cols):
                self.grid[(r, c)] = {
                    'midpt': (CELL * r + mid, CELL * c + mid),
                    'Planet': [],
                    'Star': [],
                    'Starbase': [],
                    'Station': [],
                    'Starship': []
                }
                
        # TESTING - do distances work?
        print('hey');
        print(self.check_in_bounds(0,0,0,0))
    
    '''
    Adds a new object to the grid
    '''
    def add_object(self, type, obj, x, y):
        row = math.ceil(x/CELL)
        col = math.ceil(y/CELL)
        self.grid[(row, col)][type].append(obj)
        
    '''
    Checks if an object is still in bounds.
    '''
    def check_in_bounds(self, x, y, row, col):
        return (x >= row * CELL) and (x < (row + 1) * CELL) and (y >= col * CELL) and (y < (col + 1) * CELL)
        
        
    '''
    Removes and object from the grid
    '''
    def remove_object(self, type, obj, x, y):
        row = math.ceil(x/CELL)
        col = math.ceil(y/CELL)
        self.grid[(row, col)][type].remove(obj)
        
    '''
    Moves the object to a new grid
    '''
    def update_object(self, type, obj, old_x, old_y, new_x, new_y):
        self.remove_object(type, obj, old_x, old_y)
        self.add_object(type, obj, new_x, new_y)
        