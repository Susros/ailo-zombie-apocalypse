""" Zombie Apocalypse Simulation

This program loads inputs from input file
data/input.json

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
"""

from src.Engine import *

input_file = "data/input.json"

engine = Engine()

engine.load_input_file(input_file)
engine.play()