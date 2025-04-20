from typing import Protocol
from org.bukkit.entity import Fish

class Salmon(Protocol):
    """
    Represents a salmon fish.
    """

    def get_variant(self) -> 'Variant':
        """
        Get the variant of this salmon.

        :return: salmon variant
        """
        ...

    def set_variant(self, variant: 'Variant') -> None:
        """
        Set the variant of this salmon.

        :param variant: salmon variant
        """
        ...

class Variant:
    """
    Represents the variant of a salmon - ie its size.
    """
    SMALL: 'Variant'
    MEDIUM: 'Variant'
    LARGE: 'Variant'