from typing import Dict, Optional

class WorldType:
    """
    Represents various types of worlds that may exist
    """
    NORMAL: 'WorldType'
    FLAT: 'WorldType'
    LARGE_BIOMES: 'WorldType'
    AMPLIFIED: 'WorldType'

    BY_NAME: Dict[str, 'WorldType'] = {}

    def __init__(self, name: str) -> None:
        self.name: str = name

    """
    Gets the name of this WorldType

    @return Name of this type
    """
    def get_name(self) -> str:
        ...

    """
    Gets a WorldType by its name

    @param name Name of the WorldType to get
    @return Requested WorldType, or None if not found
    """
    @staticmethod
    def get_by_name(name: str) -> Optional['WorldType']:
        ...

    @staticmethod
    def _initialize() -> None:
        ...