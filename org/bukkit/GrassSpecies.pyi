from typing import Optional, Dict

class GrassSpecies:
    """
    Represents the different types of grass.
    """
    DEAD: 'GrassSpecies'
    """
    Represents the dead looking grass.
    """
    NORMAL: 'GrassSpecies'
    """
    Represents the normal grass species.
    """
    FERN_LIKE: 'GrassSpecies'
    """
    Represents the fern-looking grass species.
    """

    data: bytes
    BY_DATA: Dict[bytes, 'GrassSpecies']

    def __init__(self, data: int) -> None:
        """
        Constructor method
        """
        ...

    def getData(self) -> bytes:
        """
        Gets the associated data value representing this species

        :return: A byte containing the data value of this grass species
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByData(data: bytes) -> Optional['GrassSpecies']:
        """
        Gets the GrassSpecies with the given data value

        :param data: Data value to fetch
        :return: The {@link GrassSpecies} representing the given value, or null
            if it doesn't exist
        :deprecated: Magic value
        """
        ...