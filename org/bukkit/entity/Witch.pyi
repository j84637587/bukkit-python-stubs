from typing import Protocol

class Raider(Protocol):
    pass

class Witch(Raider, Protocol):
    """Represents a Witch"""

    def is_drinking_potion(self) -> bool:
        """Gets whether the witch is drinking a potion
        
        Returns:
            bool: whether the witch is drinking a potion
        """
        ...