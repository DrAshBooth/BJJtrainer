'''
Created on 21 May 2014

@author: Ash

http://www.ibm.com/developerworks/linux/library/l-python-state/index.html
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/StateMachine.html

Game mechanics:
- The quicker the player responds, the more likely the move is to be successful
- Once a move is used its relative prob. of success is reduced (this encourages 
  players to use as many different moves as possible and LEARN)
'''

from trainer import Game

if __name__ == '__main__':
    g = Game()
    g.run()