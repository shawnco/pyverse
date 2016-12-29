from constants import *
from opensimplex import *
from classes.network.packet import *
from classes.network.packetcollection import *
import pygame
import sys
from classes.terrain.star import *
from classes.test import *

pc = PacketCollection()
pc.add_packet(Packet('', 1, 'first'))
pc.add_packet(Packet('', 1, 'second'))
pc.add_packet(Packet('', 2, 'third'))
pc.add_packet(Packet('', 3, 'third'))
pc.add_packet(Packet('', 1, 'third'))
pc.add_packet(Packet('', 3, 'fourth'))

t = Test()
#to_send = pc.get_packets(1)

# Setup for the Pygame window
pygame.init()
pygame.display.set_caption("No Man's Py")
screen.fill((255, 255, 255))

star = Star(2,2,'red',500,500)
running = True
while running:
    star.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
            
# Shutdown procedures
pygame.quit()
sys.exit