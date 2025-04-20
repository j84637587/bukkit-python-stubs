from typing import Protocol

class BlockData(Protocol):
    pass

class Ageable(BlockData):
    """
    'age' represents the different growth stages that a crop-like block can go
    through.
    <br>
    A value of 0 indicates that the crop was freshly planted, whilst a value
    equal to {@link #getMaximumAge()} indicates that the crop is ripe and ready
    to be harvested.
    """

    def get_age(self) -> int:
        """
        Gets the value of the 'age' property.

        Returns:
            int: the 'age' value
        """
        ...

    def set_age(self, age: int) -> None:
        """
        Sets the value of the 'age' property.

        Args:
            age (int): the new 'age' value
        """
        ...

    def get_maximum_age(self) -> int:
        """
        Gets the maximum allowed value of the 'age' property.

        Returns:
            int: the maximum 'age' value
        """
        ...