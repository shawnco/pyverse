'''
A class describing objects that are able tou receive and transmit packets.
'''
from constants import *
import pygame
from classes.network.packetcollection import *

class Router:
    def __init__(self, x, y):
        self.packets = PacketCollection()
        self.neighbors = []
        self.current_range = 0
        self.max_range = 400
        
        # Cooldown for smoother transmission display
        self.current_cooldown = 0
        self.cooldown = 500
        
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
    
    '''
    Display the router object
    '''
    def update(self):
        pygame.draw.circle(screen, COLORS['blue'], (self.x, self.y), 100)
        
        # Display the transmission range
        pygame.draw.circle(screen, COLORS['black'], (self.x, self.y), self.current_range+1, 1)      
        
        # Update transmission range after some iterations
        if self.current_cooldown == self.cooldown:
            self.current_cooldown = 0
            if self.current_range + 20 > self.max_range:
                self.current_range = 2
            else:
                self.current_range = self.current_range + 20
        else:
            self.current_cooldown = self.current_cooldown + 1
                