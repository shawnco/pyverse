'''
A packet collection is a group of packets, usually owned by a Terminal, Transceiver, or Router.
'''
from classes.network.packet import *
from classes.network.routedpacket import *

class PacketCollection:
    def __init__(self):
        self.packets = [];
        
    '''
    Add a packet to the collection
    '''
    def add_packet(self, packet):
        self.packets.append(packet);
        
    '''
    Finds, removes, and returns all packets with a specific destination
    '''
    def get_packets(self, dest):
        output = []
        for p in range(len(self.packets)):
            if self.packets[p].dest == dest:
                output.append(self.packets[p])
                self.packets.pop(p)
        return output
        