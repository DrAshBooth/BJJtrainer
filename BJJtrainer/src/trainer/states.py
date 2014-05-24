'''
Created on 21 May 2014

@author: Ash
'''
from transition import Transition
from attacks import Attack

import sys
import random

class State(object):
    def __init__(self):
        self.attacks = None
        self.transitions = None
        self.description = None
        self.name = None
        
    def trans(self):
        is_valid = False
        while not is_valid:
            print "\nWhich transition do you want to try?"
            choice = raw_input("(type '-o' for options)")
            if choice == 'quit':
                is_valid = True
                return 'quitState'
            elif choice == '-o':
                print ''
                for key in self.transitions:
                    print key
            elif choice in self.transitions:
                is_valid = True
                tempTransition = self.transitions[choice]
                if tempTransition.run():
                    print "\nNice!"
                    return tempTransition.toState
                else:
                    print "\nNot this time!"
                    return tempTransition.fromState
            else:
                print ("\nPlease enter valid option.")
        
    def attack(self):
        is_valid = False
        while not is_valid:
            print "\nWhich attack do you want to try?"
            choice = raw_input("(type '-o' for options)")
            if choice == 'quit':
                is_valid = True
                return 'quitState'
            elif choice == '-o':
                print ''
                for key in self.attacks:
                    print key
            elif choice in self.attacks:
                is_valid = True
                tempAttack = self.attacks[choice]
                if tempAttack.run():
                    print '\n' + tempAttack.succMessage
                    return 'winState'
                else:
                    print "\nNot this time!"
                    return self.name
            else:
                print ("\nPlease enter valid option.")
        
    def run(self):
        print "\n" + self.description
        if not self.transitions:
            return self.attack()
        elif not self.attacks:
            return self.trans()
        else:
            is_valid = False
            while not is_valid:
                choice = raw_input('\nWould you rather advance position or attack? (adv or att)')
                if choice == 'quit':
                    is_valid = True
                    return 'quitState'
                elif choice == 'adv':
                    is_valid = True
                    return self.trans()
                elif choice == 'att':
                    is_valid = True
                    return self.attack()
                else:
                    print ("\nPlease enter 'adv' or 'att'.")
                    
class StartState():
    def run(self):
        posNames = ['full mount', 'fully mounted', 
                    'bottom guard', 'top guard',
                    'back mount']
        print ("\n\n"
               "How would you like to start, standing or in a random position?")
        
        is_valid = False
        while not is_valid:
            choice = raw_input('Enter your choice (s or r): ')
            if choice == 'quit':
                is_valid = True
                return 'quitState'
            elif choice == 's':
                is_valid = True
                startPos = 'standing'
            elif choice == 'r':
                is_valid = True
                startPos = random.choice(posNames)
            else:
                print ("Please enter 's' or 'r'.")
        return startPos

class WinState(State):
    def run(self):
        print '\nYou win'
        is_valid = False
        while not is_valid:
            choice = raw_input('\nPlay again? (y or n):')
            if choice == 'quit':
                return 'quitState'
            elif choice == 'y':
                return 'startState'
            elif choice == 'n':
                return 'quitState'
            else:
                print ("\nPlease enter 'y' or 'n'.")
        

class QuitState(State):
    def run(self):
        print ("\n\n           We hope you enjoyed the game!\n"
                       "********************************************************")
        sys.exit() 
        
###############################################################################
################################## Positions ##################################
###############################################################################

class FullMount(State):
    def __init__(self, difficulty, adjustProb):
        self.name = "full mount"
        self.attacks = {'americana' : Attack('americana', 
                                          adjustProb(0.8, difficulty), 
                                          "You ripped you're opponents arm off!"),
                        'arm lock' : Attack('arm lock',
                                            adjustProb(0.4, difficulty), 
                                           "You ripped you're opponents arm off!")}
        self.transitions = {}
        self.description = """You have fully mounted your opponent."""

class FullyMounted(State):
    def __init__(self, difficulty, adjustProb):
        self.name = "fully mounted"
        self.attacks = {}
        self.transitions = {'trap & roll' : Transition('trap & rol', 
                                                       self.name, 
                                                       'top guard', 
                                                       adjustProb(0.6, difficulty)),
                            'elbow escape' : Transition('elbow escape', 
                                                        self.name, 
                                                        'bottom guard', 
                                                        adjustProb(0.5, difficulty))}
        self.description = """Your opponent has fully mounted you."""
        
        
class BottomGuard(State):
    def __init__(self, difficulty, adjustProb):
        self.name = "bottom guard"
        self.attacks = {'kimura' : Attack('kimura', 
                                          adjustProb(0.3, difficulty), 
                                          "You ripped you're opponents arm off!"),
                        'arm lock' : Attack('arm lock',
                                            adjustProb(0.4, difficulty), 
                                           "You ripped you're opponents arm off!"),
                        'triangle' : Attack('triangle',
                                            adjustProb(0.5, difficulty), 
                                           "You're opponent is unconscious!"),
                        'guillotine' : Attack('guillotine',
                                              adjustProb(0.3, difficulty), 
                                              "You're opponent is unconscious!")}
        self.transitions = {'elevator sweep' : Transition('elevator sweep',
                                                          self.name, 
                                                          'full mount', 
                                                          adjustProb(0.6, difficulty)),
                            'take the back' : Transition('take the back', 
                                                         self.name, 
                                                         'back mount', 
                                                         adjustProb(0.5, difficulty))}
        self.description = """You're opponent is in your guard"""
        
class TopGuard(State):
    def __init__(self, difficulty, adjustProb):
        self.name = "top guard"
        self.attacks = {}
        # TODO Add double underhook pass to side control
        self.transitions = {'open guard pass' : Transition('open guard pass',
                                                           self.name, 
                                                           'full mount', 
                                                           adjustProb(0.5, difficulty))}
        self.description = """You are in your opponent's guard"""
        
class BackMount(State):
    def __init__(self, difficulty, adjustProb):
        self.name = "back mount"
        self.attacks = {'rear naked choke' : Attack('rear naked choke', 
                                          adjustProb(0.9, difficulty), 
                                          "You choked out your opponent!")}
        self.transitions = {}
        self.description = """You have taken your opponent's back"""
        