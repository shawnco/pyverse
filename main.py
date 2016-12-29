# Imports used everywhere
from constants import *
import opensimplex
import pygame
import sys

# Terrain imports
from classes.terrain.galaxy import *
from classes.terrain.planet import *
from classes.terrain.star import *

# Networking imports
from classes.network.packet import *
from classes.network.packetcollection import *
from classes.network.routedpacket import *
from classes.network.router import *
from classes.network.snifferpacket import *
from classes.network.transceiver import *
from classes.network.transceivercollection import *

# Species and constructed objects
from classes.objects.database import *
from classes.objects.databasestation import *
from classes.objects.relay import *
from classes.objects.starbase import *
from classes.objects.species import *
from classes.objects.station import *

pc = PacketCollection()
pc.add_packet(Packet('', 1, 'first'))
pc.add_packet(Packet('', 1, 'second'))
pc.add_packet(Packet('', 2, 'third'))
pc.add_packet(Packet('', 3, 'third'))
pc.add_packet(Packet('', 1, 'third'))
pc.add_packet(Packet('', 3, 'fourth'))

# Setup for the Pygame window
pygame.init()
pygame.display.set_caption("No Man's Py")

starbase = Starbase(1,500,500)
running = True
while running:
    screen.fill(COLORS['white'])
    starbase.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
            
# Shutdown procedures
pygame.quit()
sys.exit