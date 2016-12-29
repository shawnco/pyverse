'''
A planet collection which is simply a way to handle and iterate over planets in a system
'''

from terrain.planet import *

class PlanetCollection:
    '''
    Creates an empty planet collection
    '''
    def __init__(self):
        self.planets = []
        
    '''
    Add a planet to the collection
    '''
    def add_planet(self, planet):
        self.planets.append(planet)
        
    '''
    Retrieves a planet from the collection
    '''
    def get_planet(self, id):
        for p in self.planets:
            if p.id == id:
                return p
        return False