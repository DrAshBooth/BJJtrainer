'''
Created on 21 May 2014

@author: Ash
'''

class Position(object):
    '''
    classdocs
    '''

    def __init__(self, name, description, possibleAttacks, possibleTransitions):
        '''
        Constructor
        '''
        self.beingAttacked = False
        self.attacks = []
        self.transitions = []
        
        self.description = description
        self.name = name