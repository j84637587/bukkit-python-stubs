from typing import Dict, Optional

class CoalType:
    """
    Represents the two types of coal
    """
    COAL: 'CoalType'
    CHARCOAL: 'CoalType'
    BY_DATA: Dict[bytes, 'CoalType']

    def __init__(self, data: int):
        self.data: bytes = bytes(data)

    def getData(self) -> bytes:
        """
        Gets the associated data value representing this type of coal

        :return: A byte containing the data value of this coal type
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByData(data: bytes) -> Optional['CoalType']:
        """
        Gets the type of coal with the given data value

        :param data: Data value to fetch
        :return: The CoalType representing the given value, or null if it doesn't exist
        :deprecated: Magic value
        """
        ...