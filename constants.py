'''
This file simply stores constants used throughout the program
'''
import math
import pygame

CELL = 500.0
SQRT2 = math.sqrt(2)
screen = pygame.display.set_mode((1250, 750))

COLORS = {
    'black': (0,0,0),
    'blue': (0,0,255),
    'green': (0,255,0),
    'grey': (126, 126, 126),
    'red': (255,0,0),
    'white': (255,255,255),
    'yellow': (255,255,0)
}

SIZES = {
    0: 25,
    1: 75,
    2: 150
}

PLANETS = {
    'gas': {
        'max_crystal': 1000,
        'max_gas': 10000,
        'max_metal': 100,
        'size': 75,
        'color': COLORS['red']
    },
    'rocky': {
        'max_crystal': 100,
        'max_gas': 1000,
        'max_metal': 10000,
        'size': 20,
        'color': COLORS['grey']
    },
    'terran': {
        'max_crystal': 10000,
        'max_gas': 100,
        'max_metal': 1000,
        'size': 50,
        'color': COLORS['green']
    }
}