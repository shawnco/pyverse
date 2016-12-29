'''
A class describing objects that are able tou receive and transmit packets.
'''

from packetcollection import *

class Router:
    def __init__(self):
        self.packets = PacketCollection()
        self.neighbors = []
        
    '''
    Add a neighbor to the neighbors list
    '''
    def add_neighbor(self, neighbor_id):
        self.neighbors.append(neighbor_id)
    
    '''
    Add a packet to the packet collection.
    '''
    def add_packet(self, packet):
        self.packets.add_packet(packet)
        
    '''
    Retrieve all packets with the given destination.
    '''
    def get_packets(self, dest):
        return self.packets.get_packets(dest)
    