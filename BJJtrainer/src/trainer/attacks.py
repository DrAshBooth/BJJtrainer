'''
Created on 21 May 2014

@author: Ash
'''

import random

class Attack(object):
    def __init__(self, name, succProb, succMessage):
        self.name = name
        self.succProb = succProb
        self.succMessage = succMessage;
        
    def run(self):
        return True if (random.random()<self.succProb) else False