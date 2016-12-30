'''
The Terminal is the basic object for sending and receiving packets.
'''

from classes.network.packet import *

class Terminal:
    '''
    Create a basic terminal with an ID and name
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.packets = []
        
    '''
    Writes a packet and stores it to the packet queue to be picked up by the transceiver or router
    '''
    def create_packet(self, dest, msg):
        self.packets.append(Packet(self.id, dest, msg))
        
    '''
    Receives a packet. For now it'll just write to the console the sender and contents.
    '''
    def receive_packet(self, packet):
        print("Packet received from {} with message: {}".format(packet.source, packet.message))
        
    '''
    Transmits the packets to the transceiver or router calling for it then empties the queue
    '''
    def transmit_packets(self):
        packets = self.packets
        self.packets = []
        return packets