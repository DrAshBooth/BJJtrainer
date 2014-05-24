'''
Created on 21 May 2014

@author: Ash
'''

import random

class Transition(object):
    def __init__(self, name, fromS, toS, p_success):
        self.name = name
        self.fromState = fromS
        self.toState = toS
        self.p_success = p_success
        
    def run(self):
        if (random.random()<self.p_success):
            return True
        else:
            return False