from org.bukkit import Material
from typing import Any

class Cauldron:
    """
    Represents a cauldron

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    
    CAULDRON_FULL: int
    CAULDRON_EMPTY: int

    def __init__(self) -> None:
        """
        Initializes a new instance of the Cauldron class.
        """
        ...

    def __init__(self, type: Material, data: bytes) -> None:
        """
        Initializes a new instance of the Cauldron class with specified type and data.

        :param type: the type
        :param data: the raw data value
        @deprecated Magic value
        """
        ...

    def __init__(self, data: bytes) -> None:
        """
        Initializes a new instance of the Cauldron class with specified data.

        :param data: the raw data value
        @deprecated Magic value
        """
        ...

    def is_full(self) -> bool:
        """
        Check if the cauldron is full.

        :return: True if it is full.
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the cauldron is empty.

        :return: True if it is empty.
        """
        ...

    def __str__(self) -> str:
        """
        Returns a string representation of the cauldron state.
        """
        ...

    def clone(self) -> 'Cauldron':
        """
        Clones the current instance of the Cauldron.

        :return: A clone of the current Cauldron instance.
        """
        ...