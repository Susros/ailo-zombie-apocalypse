from src.Individual import *
from src.World import *

import json
import os.path

""" Engine

This engine drives the simulation

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
version: 4.5
"""

class Engine:
    """ System engine

    Attributes:
        inputs (list): List of input to run
    """

    def __init__(self):
        """ Constructor

        Initialise inputs
        """
        self.inputs = []

    def load_input_file(self, input_file: str = "") -> None:
        """ Load json type input file

        Args:
            input_file (str): Input file
        """

        if (os.path.isfile(input_file) == False):
            print("Input file is not found.")
            exit()

        with (open(input_file)) as f:
            content = json.load(f)

        # Validate if inputs are valid
        for input_value in content['game']:
            msg = self.__validate_input(input_value)
            if (msg != '') :
                print(msg)
                exit()
            else:
                self.inputs.append(input_value)

    def get_input(self) -> None:
        """ Read input from keyboard
        """

        n = input("Enter grid size: ")

        print()
        print("Initialising zombie...")
        print("---")

        zombie_x = input("Enter zombie x coordinate: ")
        zombie_y = input("Enter zombie y coordinate: ")

        print()
        print("Initialising creatures...")
        print("---")

        creatures = []

        more_creature = 'y'

        while (more_creature.lower() == 'y'):
            creature_x = input("Enter creature x coordinate: ")
            creature_y = input("Enter creature y coordinate: ")

            creatures.append({ 'x': int(creature_x), 'y': int(creature_y) })

            print()
            more_creature = input("Do you want to add more creatures? [y/n]: ")
            print()

        moves = input("Enter zombies moves for simulation: ")

        self.inputs.append({ 
            'n': int(n), 
            'zombie': { 
                'x': int(zombie_x),
                'y': int(zombie_y)
            },
            'creatures': creatures,
            'moves': moves
        })

    def play(self) -> None:
        """ Run the world simulation
        """

        i = 0

        for inp in self.inputs:

            i += 1

            print("Simulation: ", i)
            print("World: " + str(inp['n']) + " x " + str(inp['n']))
            print()

            # Create world
            world = World(inp['n'])

            # Place zombie
            world.populate(
                Individual(is_zombie = True),
                inp['zombie']['x'], inp['zombie']['y']
            )

            # Place creatures
            for creature in inp['creatures']:
                world.populate(
                    Individual(),
                    creature['x'], creature['y']
                )

            # Simulate
            world.simulate(inp['moves'])

            # Get stats
            score, positions = world.get_stats()

            print("zombies' score: ", score)
            print("zombies' positions:")

            for position in positions:
                print("(" + str(position['x']) + ", " + str(position['y']) + ")", end = " ")

            print()
            print("---")
            print()


    def __validate_input(self, input_value: dict) -> str:
        """ Make sure the inputs are valid before simulation

        Returns:
            str : Empty if valid, message otherwise
        """
        
        n = input_value['n']

        # Check for zombie coordinates
        if (input_value['zombie']['x'] >= n or input_value['zombie']['y'] >= n):
            return "Zombie coordinate, (" + str(input_value['zombie']['x']) + ", " + str(input_value['zombie']['y']) + "), is off the grid size."

        # Check for individual
        for creature in input_value['creatures']:
            if (creature['x'] >= n or creature['y'] >= n):
                return "Creature coordinate, (" + str(creature['x']) + ", " + str(creature['y']) + "), is off the grid size."

        return ""
