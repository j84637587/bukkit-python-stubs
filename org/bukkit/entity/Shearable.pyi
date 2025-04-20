from typing import Protocol

class Shearable(Protocol):
    """
    Represents an entity which can be shorn with shears.
    """

    def is_sheared(self) -> bool:
        """
        Gets whether the entity is in its sheared state.

        Returns:
            Whether the entity is sheared.
        """
        ...

    def set_sheared(self, flag: bool) -> None:
        """
        Sets whether the entity is in its sheared state.

        Args:
            flag: Whether to shear the entity
        """
        ...