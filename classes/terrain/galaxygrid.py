'''
This class combines the concepts of a galaxy and a grid into one. This makes it easier to not only keep track of everything's location, but also update them.
'''
from constants import *
import math

class GalaxyGrid:
    '''
    Creates a new galaxy by passing it the savefile
    '''
    def __init__(self, save_file, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        
        # For the grid use ceil, just so we have that extra space.
        # For determining where to place entities, use floor.
        rows = math.floor(self.width / CELL)
        cols = math.floor(self.height / CELL)
        
        # Create the grid
        for r in range(rows):
            for c in range(cols):
                self.grid[(r, c)] = {}
                
    '''
    Add a new object to the grid.
    '''
    def add(self, obj):
        row = math.floor(obj.x / CELL)
        col = math.floor(obj.y / CELL)
        self.grid[(row, col)][obj.id] = obj
        
    '''
    Checks if an object is still in the bounds of its parent grid.
    '''
    def check(self, obj, row, col):
        x = obj.x
        y = obj.y
        return not (x >= row * CELL) and (x < (row + 1) * CELL) and (y >= col * CELL) and (y < (col + 1) * CELL)
    
    '''
    Get an object from the grid with the specified id.
    '''
    def get(self, id):
        for g in self.grid:
            if id in self.grid[g]:
                return self.grid[g][id]
        return False
        
    '''
    Removes an object from the grid.
    '''
    def remove(self, obj, row, col):
        del self.grid[(row, col)][obj.id]
        
    '''
    Updates the entire grid of entities
    '''
    def update(self):
        for g in self.grid:
            for obj in self.grid[g]:
                #print(self.grid[g][obj].id, self.grid[g][obj].x, self.grid[g][obj].y)
                self.grid[g][obj].update()
                if self.check(self.grid[g][obj], g[0], g[1]):
                    o = self.grid[g][obj]
                    #print("Obj {} needs relocation".format(o.id))
                    self.remove(o, g[0], g[1])
                    self.add(o)

'''
Notes from the programmer

The galaxy is created with a certain size, ie 10000x10000. Then it is divided into grid squares, the width of which is determined by the CELL contant.

Instead of just having one sprite group for all entities, they are instead stored into a dictionary of groups. The key of each dictionary is a tuple giving the coordinates of that sprite. 

The advantage of merging the galaxy with the grid is in the update statement. You can move and immediately update each sprite's grid location as need be.
'''
        