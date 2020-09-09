""" Individual

The individual of n x n grid world which can be either
zombie or creatures.

Author: Kelvin Zaw Moe Htat (kelvin.susros@gmail.com)
version: 4.5
"""

class Individual:
    """ The information of individual

    Attributes:
        is_zombie (bool)  : Determine if this individual is zombie
        x_coord   (int)   : Current x coordinate of the location
        y_coord   (int)   : Current y coordinate of the location
        moves     (str[]) : List of moves to make
        score     (int)   : Current score point
    """ 

    def __init__(self, is_zombie: bool = False, x_coord: int = 0, y_coord: int = 0, moves: str = ""):
        """ Constructor of the class

        This initiate the individual information.

        Args:
            is_zombie (bool)  : Determine if this individual is zombie
            x_coord   (int)   : Current x coordinate of the location
            y_coord   (int)   : Current y coordinate of the location
            moves     (str[]) : Moves to make
        """

        self.is_zombie = is_zombie
        self.x_coord   = x_coord
        self.y_coord   = y_coord
        self.moves     = list(moves.lower())
        self.score     = 0

    def set_moves(self, moves: str) -> None:
        """ Give this individual a set of moves

        This method convert moves string into list.

        Args:
            moves (str) : Moves to make
        """

        self.moves = list(moves.lower())

    def has_move(self) -> bool:
        """ Check if there is any more moves

        Returns:
            bool: True if there is stil moves, False otherwise
        """

        return len(self.moves) != 0
    
    def get_move(self) -> str:
        """ Get one move out from list

        This method grab the first move instruction from the list,
        then remove it.

        Returns:
            str: Move instruction
        """

        return self.moves.pop(0)

    def add_score(self, score: int = 0) -> None:
        """ Add point to score

        Args:
            score (int) : Score point
        """

        self.score += score