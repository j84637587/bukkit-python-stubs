from typing import Protocol

class Monster(Protocol):
    pass

class Ageable(Protocol):
    pass

class PiglinAbstract(Monster, Ageable):
    """
    Piglin / Piglin Brute.
    """

    def is_immune_to_zombification(self) -> bool:
        """
        Gets whether the piglin is immune to zombification.

        Returns:
            Whether the piglin is immune to zombification
        """
        ...

    def set_immune_to_zombification(self, flag: bool) -> None:
        """
        Sets whether the piglin is immune to zombification.

        Args:
            flag: Whether the piglin is immune to zombification
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a
        Zombified Piglin.

        When this reaches 300, the entity will be converted.

        Returns:
            conversion time

        Raises:
            IllegalStateException: if is_converting() is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a
        Zombified Piglin.

        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Args:
            time: new conversion time
        """
        ...

    def is_converting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zombified Piglin.

        Returns:
            conversion status
        """
        ...

    def is_baby(self) -> bool:
        """
        Gets whether the piglin is a baby

        Returns:
            Whether the piglin is a baby

        Deprecated:
            see Ageable.is_adult()
        """
        ...

    def set_baby(self, flag: bool) -> None:
        """
        Sets whether the piglin is a baby

        Args:
            flag: Whether the piglin is a baby

        Deprecated:
            see Ageable.set_baby() and Ageable.set_adult()
        """
        ...