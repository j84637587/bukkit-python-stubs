from typing import Protocol

class Monster(Protocol):
    pass

class Ageable(Protocol):
    pass

class Zoglin(Monster, Ageable):
    """
    Represents a Zoglin.
    """

    def is_baby(self) -> bool:
        """
        Gets whether the zoglin is a baby

        Returns:
            Whether the zoglin is a baby

        Deprecated:
            see Ageable.is_adult()
        """
        ...

    def set_baby(self, flag: bool) -> None:
        """
        Sets whether the zoglin is a baby

        Args:
            flag: Whether the zoglin is a baby

        Deprecated:
            see Ageable.set_baby() and Ageable.set_adult()
        """
        ...