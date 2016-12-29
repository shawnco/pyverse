'''
A packet is a basic piece of data that is passed among Routers, Terminals, and Transceivers.
'''

class Packet:
    '''
    Creates a new packet with a given destination and message.
    '''
    def __init__(self, source, dest, message):
        self.source = source
        self.dest = dest
        self.prev = source
        self.next = ''
        self.message = message
        