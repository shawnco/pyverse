'''
This class combines the concepts of a galaxy and a grid into one. This makes it easier to not only keep track of everything's location, but also update them.
'''
from constants import *
import math
from classes.network.router import *
from classes.network.transceiver import *
from classes.terrain.planet import *

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
                o = self.grid[g][obj]
                # If it's a transmitting type of object, we need to send it the neighbors
                if isinstance(o, (Router)):
                    # Determine which grid squares the transmission reaches
                    length = math.ceil(o.current_range / CELL)
                    
                    # Assemble a list of all objects in those grid squares
                    neighbors = []
                    for r in range(g[0] - length, g[0] + length):
                        for c in range(g[1] - length, g[1] + length):
                            if (r, c) in self.grid:
                                for obj in self.grid[(r, c)]:
                                    neighbors.append(self.grid[(r,c)][obj])
                    
                    # Pass it to the object.
                    o.update(neighbors)
                else:
                    o.update()
                if self.check(o, g[0], g[1]):
                    #print("Obj {} needs relocation".format(o.id))
                    self.remove(o, g[0], g[1])
                    self.add(o)

'''
Notes from the programmer

The galaxy is created with a certain size, ie 10000x10000. Then it is divided into grid squares, the width of which is determined by the CELL contant.

Instead of just having one sprite group for all entities, they are instead stored into a dictionary of groups. The key of each dictionary is a tuple giving the coordinates of that sprite. 

The advantage of merging the galaxy with the grid is in the update statement. You can move and immediately update each sprite's grid location as need be.
'''
        