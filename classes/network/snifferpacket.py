'''
A sniffer packet is a type of packet that tracks down a route
'''

from classes.network.packet import *

class SnifferPacket(Packet):
    '''
    Creates the packet
    '''
    def __init__(self, source, dest):
        self.source = soruce
        self.dest = dest
        self.prev = source
        self.next = ''
        self.msg = 'SNIFFING ROUTE TO ' + dest
        self.route = []
        
    '''
    Checks for loops in the route and removes any found
    '''
    def check_route(self, id):
        if id in self.route:
            self.route = self.route[self.route.index(id):]
        else:
            self.route.append(id)