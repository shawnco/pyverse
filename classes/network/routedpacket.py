'''
A routed packet is one which has an intended route to get it from start to end.

These are usually preceded by a sniffer packet determining its path.
'''
from classes.network.packet import *

class RoutedPacket(Packet):
    def __init__(self, source, dest, message, route):
        super.__init__(source, dest, message)
        self.route = route
        self.step = 0
        