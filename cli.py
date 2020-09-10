""" Zombie Apocalypse Simulation

This is CLI interactive application for simulation

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
"""

from src.Engine import *

cont = 'y'

while (cont.lower() == 'y'):
    engine = Engine()

    engine.get_input()
    engine.play()

    cont = input("Start another simulation? [y/n]: ")
