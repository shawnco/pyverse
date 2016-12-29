'''
A database station is a type of station designed to hold information.
'''

from classes.network.router import *
from classes.objects.database import *
from classes.objects.station import *

class DatabaseStation(Station, Router):
    '''
    Initialize the database
    '''
    def __init__():
        self.database = Database()