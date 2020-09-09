
from src.Individual import *

""" Test for Individual

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
"""

# Prepare test cases
x = 3
y = 1
is_zombie = True
moves = "DDUULLRR"

def test_coord():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    assert x == individual.x_coord and y == individual.y_coord

def test_moves():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    for m in moves:
        assert m.lower() == individual.get_move()

def test_is_zombie():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    assert is_zombie == individual.is_zombie

def test_has_move():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    assert individual.has_move() == True

def test_has_no_move():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    while individual.has_move():
        individual.get_move()
    
    assert individual.has_move() == False

def test_add_score():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = moves)
    individual.add_score(10)

    assert individual.score == 10

def test_set_moves():
    individual = Individual(is_zombie = is_zombie, x_coord = x, y_coord = y, moves = "")

    individual.set_moves(moves)

    for m in moves:
        assert m.lower() == individual.get_move()

    