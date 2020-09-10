
from src.World import *
from src.Individual import *

""" Test for World

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
"""

def test_populate():
    w = World(4)

    w.populate(
        Individual(),
        1, 3
    )

    assert 1 == len(w.get_population())

def test_queeu_when_zombie_is_populated():
    w = World(4)

    w.populate(
        Individual(is_zombie = True),
        1, 3
    )

    assert 1 == len(w.get_queue())

def test_simulation():
    w = World(4)

    w.populate(
        Individual(is_zombie = True),
        2, 1
    )

    w.populate(
        Individual(),
        1, 2
    )

    w.simulate(moves = "DLUURR")

    score, positions = w.get_stats()

    # One victim
    assert 1 == score

    # Two zombies
    assert 2 == len(positions)

    # First at (3, 0)
    assert 3 == positions[0]['x']
    assert 0 == positions[0]['y']

    # Second at (2, 1)
    assert 2 == positions[1]['x']
    assert 1 == positions[1]['y']

