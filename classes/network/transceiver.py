'''
A Transceiver is a device that allows communication between terminals and routers
'''
import pygame
from constants import *
from classes.network.packet import *
from classes.network.packetcollection import *

class Transceiver:
    '''
    Creates a transceiver
    '''
    def __init__(self, x, y):
        self.packets = PacketCollection()
        self.x = x
        self.y = y
        self.current_cooldown = 0
        self.current_range = 0
        self.max_range = 500
        self.cooldown = 25
        
    '''
    Finds all packets and distributes them into the packet collection
    '''
    def distribute_packets(self):
        pass
    
    '''
    Receives packets
    '''
    def collect_packets(self):
        pass
    
    '''
    Display the transmission wave
    '''
    def update(self):
        pygame.draw.circle(screen, COLORS['black'], (self.x, self.y), self.current_range+1, 1)
        if self.current_cooldown == self.cooldown:
            self.current_cooldown = 0
            if self.current_range + 20 > self.max_range:
                self.current_range = 2
            else:
                self.current_range = self.current_range + 20
        else:
            self.current_cooldown = self.current_cooldown + 1