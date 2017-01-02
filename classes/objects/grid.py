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
        
        # Create the grid
        for r in range(rows):
            for c in range(cols):
                self.grid[(r, c)] = {}
    
    '''
    Adds a new object to the grid
    '''
    def add_object(self, obj, row, col):
        self.grid[(row, col)][obj.id] = obj
        
    '''
    Checks if an object is still in bounds.
    '''
    def check_in_bounds(self, x, y, row, col):
        return (x >= row * CELL) and (x < (row + 1) * CELL) and (y >= col * CELL) and (y < (col + 1) * CELL)
        
        
    '''
    Removes and object from the grid
    '''
    def remove_object(self, obj, row, col):
        del self.grid[(row, col)][obj.id]
        
    '''
    Checks all object positions to see if they need to be updated in the grid.
    '''
    def update(self):
        for g in self.grid:
            for obj in self.grid[g]:
                if self.check_in_bounds(self.grid[g][obj].x, self.grid[g][obj].y, g[0], g[1]):
                    self.update_object(self.grid[g][obj], g[0], g[1])
        
        
    '''
    Moves the object to a new grid
    '''
    def update_object(self, obj, old_x, old_y):
        # Calculate the new grid location
        new_x = math.ceil(old_x/CELL)
        new_y = math.ceil(old_y/CELL)
        
        self.remove_object(obj, old_x, old_y)
        self.add_object(obj, new_x, new_y)
        