'''
Created on 21 May 2014

@author: Ash
'''

from position import Position

class Game(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.positions = self.initialisePositions()

     
    def run(self):
        print ("""Welcome to the BJJ brain trainer!\n\n
                 How would you like to start, standing or in a random position?""")

        is_valid = False
        while not is_valid :
                choice = int ( raw_input('Enter your choice (s or r): ') )
                if choice == 's':
                    # do standing stuff
                    is_valid = True
                    pass
                elif choice == 'r':
                    # random pos
                    is_valid = True
                    pass
                else:
                    print ("Please enter 's' or 'r'.")
    
    def initialisePositions(self):
        positions = [Position()]
        return positions