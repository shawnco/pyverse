'''
The Galaxy object encapsulates the entire program. It also handles loading and saving of the save files.
'''
import pygame

class Galaxy:
    '''
    Creates a new galaxy by passing it the savefile
    '''
    def __init__(self, save_file):
        # This list holds all the top-level 
        self.entities = pygame.sprite.Group()
        
    '''
    Adds an object to the entity collection
    '''
    def add_object(self, obj):
        self.entities.add(obj)
    
    '''
    Runs the L-system generator to create a new planet
    '''
    def generate_planet(self):
        pass
    
    '''
    Runs the random number generator to create a new star
    '''
    def generate_star(self):
        pass
    
    '''
    Loads the galaxy file into memory
    '''
    def load_file(self):
        pass
    
    '''
    Saves the galaxy to memory
    '''
    def save_file(self):
        pass
    
    '''
    Calls the update function on all objects in the collection
    '''
    def update(self):
        self.entities.update()
        