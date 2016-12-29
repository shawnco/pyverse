'''
The database holds information retrieved by the fleet.
'''

class Database:
    '''
    Create the database, which is a dictionary of dictionaries
    '''
    def __init__(self):
        self.database = {}

    '''
    Adds a new entry in a page in the dictionary
    '''
    def add_to_dict(self, page, key, value):
        self.database[page][key] = value
    
    '''
    Create a new page in the dictionary
    '''
    def create_page(self, page):
        self.database[page] = {}
        
    '''
    Updates existing information in the dictionary
    '''
    def update_dict(self, page, key, value):
        self.database[page][key] = value