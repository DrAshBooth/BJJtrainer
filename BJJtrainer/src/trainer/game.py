'''
Created on 21 May 2014

@author: Ash
'''

from statemachine import StateMachine
from states import FullMount, FullyMounted, BottomGuard, TopGuard, BackMount, StartState, WinState, QuitState

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.sm = StateMachine()
        self.posNames = ['full mount', 'fully mounted', 
                         'bottom guard', 'top guard',
                         'back mount']
        
    def adjustProb(self, original, diffi):
            minVal = 0.2*original
            return original-(original-minVal)*diffi

    def run(self):
        
        self.sm.setStart('startState')
        self.sm.addState('startState', StartState(), True)
        self.sm.addState(self.posNames[0], FullMount(0,self.adjustProb))
        self.sm.addState(self.posNames[1], FullyMounted(0,self.adjustProb))
        self.sm.addState(self.posNames[2], BottomGuard(0,self.adjustProb))
        self.sm.addState(self.posNames[3], TopGuard(0,self.adjustProb))
        self.sm.addState(self.posNames[4], BackMount(0,self.adjustProb))
        self.sm.addState('winState', WinState())
        self.sm.addState('quitState', QuitState(), True)
        
        print ("\n\n"
               "********************************************************"
               "\n         Welcome to the BJJ brain trainer!\n"
               "********************************************************"
               "\n"
               "Enter 'quit' at any time to quit")
        while True:
            self.sm.run()
        
        