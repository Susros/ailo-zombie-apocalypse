import numpy as np

from src.individual import *

""" World

The world of the zombie apocalypse. In this world there is
n x n grid.

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
version: 4.5
"""

class World:
    """ Zombie apocalypse simuation

    Attributes:
        N          (int)   : Size of the world
        map        (numpy) : N x N grid map of the world
        queue      (List)  : Queue for zombie to action
        population (List)  : List of all individuals
    """

    def __init__(self, N: int = 0):
        """ Constructor of world class

        Initialse the world.

        Args:
            N (int) : Size of the world
        """

        self.N          = N
        self.queue      = []
        self.population = []

        # Create map for the world
        # The location where there is no individuals are noted
        # as -1. Otherwise, the index of the population.
        self.map = np.negative(
            np.ones( (N, N), np.int32 )
        )
    
    def populate(self, individual: Individual, x_coord: int = 0, y_coord: int = 0) -> None:
        """ Populate the world with an individual.

        Args:
            individual (Individual) : Individual of the world. Either a zombie or victim.
            x_coord    (int)        : The position, x coordinate, of the individual
            y_coord    (int)        : The position, y coordinate, of the individual
        """

        # Save coordinates
        individual.x_coord = x_coord
        individual.y_coord = y_coord

        # Add to population
        self.population.append(individual)

        # Get the population index of this individual
        population_index = len(self.population) - 1

        # Place the individual on the map
        self.map[x_coord][y_coord] = population_index

        # Add zombie to the queue to action
        if (individual.is_zombie):
            self.__enqueue(individual)

    def simulate(self, moves: str = "") -> None:
        """ Simulate the world.

        This simulate the world with specified moves. Those moves are for 
        zombie

        Args:
            moves (str) : Moves to move around in this world
        """

        # Simulate until all zombie have moved
        while(self.__is_queue_empty() == False):

            zombie = self.__dequeue()

            # Give this zombie a moves instruction
            zombie.set_moves(moves)

            # Get the current population index
            zombie_population_index = self.map[zombie.x_coord][zombie.y_coord]

            # Prepare to start moving
            self.map[zombie.x_coord][zombie.y_coord] = -1

            while(zombie.has_move()):
                direction = zombie.get_move()
                
                self.__move(individual = zombie, direction = direction)

                # Check if there is an individual in current location
                individual_index = self.map[zombie.x_coord][zombie.y_coord]

                if (individual_index != -1):
                    individual = self.population[individual_index]

                    # Check if that individual is creature
                    if (individual.is_zombie == False):
                        zombie.add_score(1)

                        # Infected
                        individual.is_zombie = True
                        individual.set_moves(moves)
                        self.__enqueue(individual)
            
            # Final position of the zombie
            self.map[zombie.x_coord][zombie.y_coord] = zombie_population_index
            
    def __enqueue(self, individual: Individual) -> None:
        """ Add individual to the action queue.

        Args:
            individual (Individual) : Individual of the world
        """

        self.queue.append(individual)
        
    def __dequeue(self) -> Individual:
        """ Get individual from the action queue.

        Returns:
            Individual: Individual to action
        """

        return self.queue.pop(0)

    def __is_queue_empty(self) -> bool:
        """ Check if action queue is emtpy

        Returns:
            bool : True if queue is empty, False otherwise.
        """

        return len(self.queue) == 0

    def __move(self, individual: Individual, direction: str) -> None:
        """ Move the individual around the map.

        This moves the individual according to the direction given.
        Zombie can move from one edge through the edge.

        Args:
            individual (Individual) : Individual of the world
            direction  (str)        : Direction for individual to move
        """

        # Make sure to lowercase
        direction = direction.lower()

        # Going Up
        if (direction == 'u'):
            if (individual.y_coord == 0):
                if (individual.is_zombie):
                    individual.y_coord = self.N - 1
            else:
                individual.y_coord -= 1

        # Going Down
        if (direction == 'd'):
            if (individual.y_coord == self.N - 1):
                if (individual.is_zombie):
                    individual.y_coord = 0
            else:
                individual.y_coord += 1

        # Going Left
        if (direction == 'l'):
            if (individual.x_coord == 0):
                if (individual.is_zombie):
                    individual.x_coord = self.N - 1
            else:
                individual.x_coord -= 1

        # Going Right
        if (direction == 'r'):
            if (individual.x_coord == self.N - 1):
                if (individual.is_zombie):
                    individual.x_coord = 0
            else:
                individual.x_coord += 1
