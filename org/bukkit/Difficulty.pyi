from typing import Dict, Optional

class Difficulty:
    """
    Represents the various difficulty levels that are available.
    """

    PEACEFUL: 'Difficulty'
    """
    Players regain health over time, hostile mobs don't spawn, the hunger
    bar does not deplete.
    """

    EASY: 'Difficulty'
    """
    Hostile mobs spawn, enemies deal less damage than on normal difficulty,
    the hunger bar does deplete and starving deals up to 5 hearts of
    damage. (Default value)
    """

    NORMAL: 'Difficulty'
    """
    Hostile mobs spawn, enemies deal normal amounts of damage, the hunger
    bar does deplete and starving deals up to 9.5 hearts of damage.
    """

    HARD: 'Difficulty'
    """
    Hostile mobs spawn, enemies deal greater damage than on normal
    difficulty, the hunger bar does deplete and starving can kill players.
    """

    value: int
    BY_ID: Dict[int, 'Difficulty']

    def __init__(self, value: int) -> None:
        ...

    def getValue(self) -> int:
        """
        Gets the difficulty value associated with this Difficulty.
        
        :return: An integer value of this difficulty
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByValue(value: int) -> Optional['Difficulty']:
        """
        Gets the Difficulty represented by the specified value
        
        :param value: Value to check
        :return: Associative Difficulty with the given value, or null if
            it doesn't exist
        :deprecated: Magic value
        """
        ...