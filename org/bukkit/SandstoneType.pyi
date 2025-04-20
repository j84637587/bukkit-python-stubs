from typing import Dict, Optional

class SandstoneType:
    """
    Represents the three different types of Sandstone
    """
    CRACKED: 'SandstoneType'
    GLYPHED: 'SandstoneType'
    SMOOTH: 'SandstoneType'
    BY_DATA: Dict[bytes, 'SandstoneType']

    data: bytes

    def __init__(self, data: int) -> None:
        """
        Constructor method for SandstoneType.
        """
        ...

    def getData(self) -> bytes:
        """
        Gets the associated data value representing this type of sandstone

        :return: A byte containing the data value of this sandstone type
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByData(data: bytes) -> Optional['SandstoneType']:
        """
        Gets the type of sandstone with the given data value

        :param data: Data value to fetch
        :return: The SandstoneType representing the given value, or null if it doesn't exist
        :deprecated: Magic value
        """
        ...