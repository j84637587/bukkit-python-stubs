from typing import Dict, Optional

class CropState:
    """
    Represents the different growth states of crops
    """
    SEEDED: int = 0x0
    """
    State when first seeded
    """
    GERMINATED: int = 0x1
    """
    First growth stage
    """
    VERY_SMALL: int = 0x2
    """
    Second growth stage
    """
    SMALL: int = 0x3
    """
    Third growth stage
    """
    MEDIUM: int = 0x4
    """
    Fourth growth stage
    """
    TALL: int = 0x5
    """
    Fifth growth stage
    """
    VERY_TALL: int = 0x6
    """
    Almost ripe stage
    """
    RIPE: int = 0x7
    """
    Ripe stage
    """

    data: int
    BY_DATA: Dict[int, 'CropState']

    def __init__(self, data: int) -> None:
        """
        Constructor
        """
        ...

    def getData(self) -> int:
        """
        Gets the associated data value representing this growth state

        :return: A byte containing the data value of this growth state
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByData(data: int) -> Optional['CropState']:
        """
        Gets the CropState with the given data value

        :param data: Data value to fetch
        :return: The CropState representing the given value, or null if it doesn't exist
        :deprecated: Magic value
        """
        ...