from org.bukkit.entity import Zombie

class Husk(Zombie):
    """
    Represents a Husk - variant of {@link Zombie}.
    """

    def is_converting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zombie as a
        result of being underwater.

        @return conversion status
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Zombie
        as a result of being underwater.

        When this reaches 0, the entity will be converted.

        @return conversion time
        @throws IllegalStateException if {@link #isConverting()} is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a Zombie
        as a result of being underwater.

        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        @param time new conversion time
        """
        ...