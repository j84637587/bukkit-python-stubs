from typing import Optional
from org.bukkit.entity import Monster, Ageable
from org.jetbrains.annotations import Contract, Nullable

class Zombie(Monster, Ageable):
    """
    Represents a Zombie.
    """

    @Deprecated(since="1.16.2")
    def is_baby(self) -> bool:
        """
        Gets whether the zombie is a baby.

        :return: Whether the zombie is a baby
        """
        ...

    @Deprecated(since="1.16.2")
    def set_baby(self, flag: bool) -> None:
        """
        Sets whether the zombie is a baby.

        :param flag: Whether the zombie is a baby
        """
        ...

    @Deprecated(since="1.10.2")
    def is_villager(self) -> bool:
        """
        Gets whether the zombie is a villager.

        :return: Whether the zombie is a villager
        """
        ...

    @Deprecated(since="1.9")
    @Contract("_ -> fail")
    def set_villager(self, flag: bool) -> None:
        """
        :param flag: flag
        """
        ...

    @Deprecated(since="1.10.2")
    @Contract("_ -> fail")
    def set_villager_profession(self, profession: 'Villager.Profession') -> None:
        """
        :param profession: profession
        """
        ...

    @Deprecated(since="1.10.2")
        @Contract("-> null")
    def get_villager_profession(self) -> Optional['Villager.Profession']:
        """
        :return: profession
        """
        ...

    def is_converting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Drowned as a
        result of being underwater.

        :return: conversion status
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a Drowned
        as a result of being underwater.

        When this reaches 0, the entity will be converted.

        :return: conversion time
        :raises IllegalStateException: if {@link #isConverting()} is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a Drowned
        as a result of being underwater.

        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        :param time: new conversion time
        """
        ...

    def can_break_doors(self) -> bool:
        """
        Gets whether this zombie can break doors.

        :return: Whether this zombie can break doors
        """
        ...

    def set_can_break_doors(self, flag: bool) -> None:
        """
        Sets whether this zombie can break doors.

        This will be ignored if the entity is a Drowned. Will also stop the action if
        the entity is currently breaking a door.

        :param flag: Whether this zombie can break doors
        """
        ...