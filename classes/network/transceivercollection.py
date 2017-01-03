'''
Holds a collection of transceivers, which permit interaction between Terminals and Routers
'''

from classes.network.transceiver import *

class TransceiverCollection:
    '''
    Creates an empty transceiver collection
    '''
    def __init__(self):
        self.transceivers = []
        
    '''
    Adds a transceiver to the collection
    '''
    def add_transceiver(self, t):
        self.transceivers.append(t)
        
    '''
    Fetches the transceiver with the given index
    '''
    def get_transceiver(self, i):
        return self.transceivers[i]
    
    '''
    Call the update for each transceiver
    '''
    def update(self):
        for t in self.transceivers:
            t.update()