from typing import Protocol

class Fish(Protocol):
    pass

class Tadpole(Fish, Protocol):
    """
    A baby {@link Frog}.
    """

    def get_age(self) -> int:
        """
        Gets the age of this mob.

        Returns:
            int: Age
        """
        ...

    def set_age(self, age: int) -> None:
        """
        Sets the age of this mob.

        Args:
            age (int): New age
        """
        ...
