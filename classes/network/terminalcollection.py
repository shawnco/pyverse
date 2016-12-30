'''
A terminal collection object, for handling groups of them and also receiving all their packets at once
'''

from classes.network.terminal import *

class TerminalCollection:
    '''
    Create the terminal collection as a list of terminals
    '''
    def __init__(self):
        self.terminals = []
        
    '''
    Add a terminal
    '''
    def add_terminal(self, t):
        self.terminals.append(t)
        
    '''
    Collects packets from all terminals and returns the list
    '''
    def collect_packets(self):
        packets = []
        for t in self.terminals:
            packets.append(t.transmit_packets())
        return packets
        
    '''
    Distribute packets to their respective destination terminals
    '''
    def distribute_packets(self, packets):
        for p in packets:
            for t in self.terminals:
                if p.dest == t.id:
                    t.receive_packet(p)