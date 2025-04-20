from typing import Protocol
from org.bukkit import NamespacedKey

class Keyed(Protocol):
    """
    Represents an object which has a NamespacedKey attached to it.
    """

    def getKey(self) -> NamespacedKey:
        """
        Return the namespaced identifier for this object.

        :return: this object's key
        """
        ...