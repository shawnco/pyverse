'''
Holds a collection of transceivers, which permit interaction between Terminals and Routers
'''

from classes.network.transceiver import *

class TransceiverCollection:
    '''
    Creates an empty transceiver collection
    '''
    def __init__(self, id):
        self.id
        self.transceivers = []
        
    '''
    Adds a transceiver to the collection
    '''
    def add_transceiver(self, t):
        self.transceivers.append(t)
        
    '''
    Fetches the transceiver with the given id
    '''
    def get_transceiver(self, id):
        for t in self.transceivers:
            if t.id == id:
                return t
        return False