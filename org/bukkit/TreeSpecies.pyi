from typing import Optional, Dict

"""
Represents the different species of trees regardless of size.

@deprecated Deprecated, see usage methods for replacement(s)
"""
class TreeSpecies:
    """
    Represents the common tree species.
    """
    GENERIC = 0x0
    """
    Represents the darker barked/leaved tree species.
    """
    REDWOOD = 0x1
    """
    Represents birches.
    """
    BIRCH = 0x2
    """
    Represents jungle trees.
    """
    JUNGLE = 0x3
    """
    Represents acacia trees.
    """
    ACACIA = 0x4
    """
    Represents dark oak trees.
    """
    DARK_OAK = 0x5

    _data: int
    _BY_DATA: Dict[int, 'TreeSpecies'] = {}

    def __init__(self, data: int) -> None:
        self._data = data

    """
    Gets the associated data value representing this species

    @return A byte containing the data value of this tree species
    @deprecated Magic value
    """
    def get_data(self) -> int:
        ...

    """
    Gets the TreeSpecies with the given data value

    @param data Data value to fetch
    @return The {@link TreeSpecies} representing the given value, or null
        if it doesn't exist
    @deprecated Magic value
    """
    @staticmethod
    def get_by_data(data: int) -> Optional['TreeSpecies']:
        ...