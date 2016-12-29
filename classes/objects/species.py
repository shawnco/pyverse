'''
An implementation for species.
'''

class Species:
    '''
    Creates a species object
    '''
    def __init__(self, id, name, origin_planet):
        self.id = id
        self.name = name
        self.origin_planet = origin_planet