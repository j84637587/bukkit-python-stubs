from typing import Protocol

class Redstone(Protocol):
    """
    Indicated a Material that may carry or create a Redstone current
    """

    def is_powered(self) -> bool:
        """
        Gets the current state of this Material, indicating if it's powered or
        unpowered

        :return: true if powered, otherwise false
        """
        ...