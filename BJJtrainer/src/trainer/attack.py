'''
Created on 21 May 2014

@author: Ash
'''

import random

class Attack(object):
    '''
    classdocs
    '''
    
    def __init__(self, name, succProb):
        '''
        Constructor
        '''
        self.name = name
        self.succProb = succProb
        
    def go(self):
        return True if (random.random()<self.succProb) else False