from org.bukkit.entity import Zombie
from org.bukkit import OfflinePlayer
from typing import Optional

class ZombieVillager(Zombie):
    """
    Represents a {@link Zombie} which was once a {@link Villager}.
    """

    def set_villager_profession(self, profession: Optional['Villager.Profession']) -> None:
        """
        Sets the villager profession of this zombie.
        """
        ...

    def get_villager_profession(self) -> Optional['Villager.Profession']:
        """
        Returns the villager profession of this zombie.

        @return: the profession or null
        """
        ...

    def get_villager_type(self) -> 'Villager.Type':
        """
        Gets the current type of this villager.

        @return: Current type.
        """
        ...

    def set_villager_type(self, type: 'Villager.Type') -> None:
        """
        Sets the new type of this villager.

        @param type: New type.
        """
        ...

    def is_converting(self) -> bool:
        """
        Get if this entity is in the process of converting to a Villager as a
        result of being cured.

        @return: conversion status
        """
        ...

    def get_conversion_time(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a
        Villager as a result of being cured.

        When this reaches 0, the entity will be converted.

        @return: conversion time
        @raises IllegalStateException: if {@link #isConverting()} is false.
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a
        Villager as a result of being cured.

        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        @param time: new conversion time
        """
        ...

    def get_conversion_player(self) -> Optional[OfflinePlayer]:
        """
        Gets the player who initiated the conversion.

        @return: the player, or <code>null</code> if the player is unknown or the
        entity isn't converting currently
        """
        ...

    def set_conversion_player(self, conversion_player: Optional[OfflinePlayer]) -> None:
        """
        Sets the player who initiated the conversion.
        <p>
        This has no effect if this entity isn't converting currently.

        @param conversion_player: the player
        """
        ...