'''
A Transceiver is a device that allows communication between terminals and routers
'''

from classes.network.packet import *
from classes.network.packetcollection import *

class Transceiver:
    '''
    Creates a transceiver
    '''
    def __init__(self):
        self.packets = PacketCollection()
        
    '''
    Finds all packets and transmits them to the universe
    '''
    def distribute_packets(self):
        pass
    
    '''
    Receives packets
    '''
    def collect_packets(self):
        pass