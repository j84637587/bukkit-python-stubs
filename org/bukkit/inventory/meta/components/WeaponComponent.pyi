from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.jetbrains.annotations import ApiStatus

"""
Represents a component which can turn any item into a weapon.
"""

class WeaponComponent(ConfigurationSerializable):
    """
    Get the weapon damage per attack.

    @return: the damage per attack
    """

    def get_item_damage_per_attack(self) -> int: ...

    """
    Set the weapon damage per attack.

    @param damage: the damage to set. Must be 0 or a positive integer
    """
    def set_item_damage_per_attack(self, damage: int) -> None: ...

    """
    Get the time in seconds which this weapon disabled blocking for.

    @return: the blocking disable time in seconds
    """
    def get_disable_blocking_for_seconds(self) -> float: ...

    """
    Set the time in seconds which this weapon disabled blocking for.

    @param time: the blocking disable time in seconds
    """
    def set_disable_blocking_for_seconds(self, time: float) -> None: ...
