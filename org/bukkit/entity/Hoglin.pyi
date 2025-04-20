from org.bukkit.entity import Animals, Enemy

class Hoglin(Animals, Enemy):
    """
    Represents a Hoglin.
    """

    def is_immune_to_zombification(self) -> bool:
        """
        Gets whether the hoglin is immune to zombification.

        :return: Whether the hoglin is immune to zombification
        """
        ...

    def set_immune_to_zombification(self, flag: bool) -> None:
        """
        Sets whether the hoglin is immune to zombification.

        :param flag: Whether the hoglin is immune to zombification
        """
        ...

    def is_able_to_be_hunted(self) -> bool:
        """
        Get whether the hoglin is able to be hunted by piglins.

        :return: Whether the hoglin is able to be hunted by piglins
        """
        ...

    def set_is_able_to_be_hunted(self, flag: bool) -> None:
        """
        Sets whether the hoglin is able to be hunted by piglins.

        :param flag: Whether the hoglin is able to be hunted by piglins.
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Zoglin.

        When this reaches 300, the entity will be converted.

        :return: conversion time
        :raises IllegalStateException: if is_converting() is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a Zoglin.

        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        :param time: new conversion time
        """
        ...

    def is_converting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Zoglin.

        :return: conversion status
        """
        ...
